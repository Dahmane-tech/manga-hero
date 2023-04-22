import scrapy


class MangaSpider(scrapy.Spider):
    name = 'manga'

    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['mangalek.net']
        self.start_urls = [start_url] if start_url else ['https://mangalek.net/manga/isekai-de-tochi-wo-katte-noujou-wo-tsukurou/']

    def parse(self, response):
        title = response.css('meta[property="og:title"]::attr(content)').get()
        description = response.css('meta[property="og:description"]::attr(content)').get()
        image_url = response.css('meta[property="og:image"]::attr(content)').get()

        chapters = []
        for chapter_link in response.css('li.wp-manga-chapter a::attr(href)').getall():
            chapter = yield scrapy.Request(chapter_link, callback=self.parse_chapter, meta={'title': title})
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
        chapter_title = response.css('h1#chapter-heading::text').get().strip()

        # Extract the image URLs from the current page
        images = response.css('img.wp-manga-chapter-img::attr(src)').getall()
        images = [img.strip() for img in images]

        chapter = {
            'chapter_title': chapter_title,
            'images': images
        }

        return chapter
