import scrapy

class MangaSpider(scrapy.Spider):
    name = 'manga'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['arabshentai.com']
        self.start_urls = [start_url] if start_url else ['https://mangalek.net/manga/isekai-de-tochi-wo-katte-noujou-wo-tsukurou/']

    def parse(self, response):
        title = response.css('span.valor::text').get()
        processed_string = ''.join(c for c in title if c.isalpha())  
        title = ' '.join(w.capitalize() for w in processed_string.split())
        description = response.css('div.wp-content > ul > li::text').get() or  response.css('div.sbox div.wp-content blockquote p::text').get() or response.css('div.sbox div.wp-content p::text').get() 
        image_url = response.css('img[itemprop="image"]::attr(src)').get() 

        chapter_links = response.css('div.sbox ul li a::attr(href)').getall()
        chapters = []
        for chapter_link in chapter_links:
            chapter =  yield scrapy.Request(chapter_link, callback=self.parse_chapter, meta={'title': title})
            chapters.append(chapter)
        yield {
            'title': title,
            'description': description,
            'image_url': image_url,
            'chapters': chapters
            
        }

    def parse_chapter(self, response):
        title = response.meta.get('title')

        # Extract the chapter title
        chapter_title = response.css('h1.chapter_name::text').get().strip()

        # Extract the image URLs from the current page
        images = response.css('img.wp-manga-chapter-img.effect-fade.img-responsive.lazyload::attr(data-src)').getall()

        chapter ={
            
            'chapter_title': chapter_title,
            'images': images
        }
        return chapter
