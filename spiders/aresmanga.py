import scrapy


class MangaSpider(scrapy.Spider):
    name = 'manga'

    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['aresmanga.net']
        self.start_urls = [start_url] if start_url else ['https://aresmanga.net/series/apotheosis/']

    def parse(self, response):
        title = response.css('h1.entry-title::text').get()
        description =  response.css('div.entry-content.entry-content-single[itemprop="description"] p::text').get() if response.css('div.entry-content.entry-content-single[itemprop="description"] p::text').get() else response.css('div[itemprop="description"] p::text').get() if response.css('div[itemprop="description"] p::text').get()  else response.css('div.entry-content.entry-content-single p::text').get()
        image_url = response.css('div.thumb img::attr(src)').get()

        chapters = []
        print(type(response.css('div.eph-num a::attr(href)').getall()[1:]))
        chapters_links = response.css('div.eph-num a::attr(href)').getall()[1:]
        for chapter_link in chapters_links:
            chapter = yield scrapy.Request(chapter_link, callback=self.parse_chapter, meta={'title': title})
            chapters.append(chapter)

        yield {
            'title': title,
            'description': description,
            'image_url': image_url,
            'chapters': chapters
        }

    def parse_chapter(self, response):
        

        # Extract the chapter title
        chapter_title = response.css('h1.entry-title::text').get()

        # Extract the image URLs from the current page
        images = response.css('div#readerarea img::attr(src)').getall()
        images = [img.strip() for img in images]

        chapter = {
            'chapter_title': chapter_title,
            'images': images
        }

        return chapter
