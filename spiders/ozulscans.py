import scrapy

class MangaSpider(scrapy.Spider):
    name = 'manga'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['ozulscans.com']
        self.start_urls = [start_url] if start_url else ['https://ozulscans.com/manga/crazy-leveling-system/']

    def parse(self, response):
        title = response.css('h1.entry-title::text').get().strip()
        processed_string = ''.join(c for c in title if c.isalpha())  
        title = ' '.join(w.capitalize() for w in processed_string.split())
        description = response.css("meta[property='og:description']::attr(content)").get().strip()
        image_url = response.css("meta[property='og:image:secure_url']::attr(content)").get()

        chapter_links = response.css('div.eplister div.chbox div.eph-num a::attr(href)').getall()
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
        chapter_title  = response.css('h1.entry-title::text').get().strip()

        # Extract the image URLs from the current page
        images = response.css('img.alignnone.size-medium::attr(src)').getall() or response.css('img.ts-main-image.curdown::attr(src)') or response.css('img.alignnone.size-full::attr(src)').getall()
        images = [img.strip() for img in images]
        chapter ={
            
            'chapter_title': chapter_title,
            'images': images
        }
        return chapter