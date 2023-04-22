import scrapy

class MangaSpider(scrapy.Spider):
    name = 'manga'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['arabtoons.net']#//*//
        self.start_urls = [start_url] if start_url else ['https://arabtoons.net/manga/caffeine/']#//*//

    def parse(self, response):
        title = response.css('div.post-title h1::text').get().strip()#//*//
     
        description = response.css('div.tabcontent div.summary-text::text').get().strip()#//*//
        image_url = response.css("meta[property='og:image']::attr(content)").get()#//*//

        chapter_links = response.css('li.wp-manga-chapter a::attr(href)').getall()#//*//
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
        chapter_title = response.css('div.c-breadcrumb ol.breadcrumb li.active::text').get().strip()#//*//

        # Extract the image URLs from the current page
        images = response.css('div.page-break.no-gaps img::attr(src)').getall()#//*//
        images = [img.strip() for img in images]
        chapter ={
            
            'chapter_title': chapter_title,
            'images': images
        }
        return chapter