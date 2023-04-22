import scrapy
class MySpider(scrapy.Spider):
    name = 'team1x1.fun'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['azoranov.com']
        self.start_urls = [start_url] if start_url else ['https://azoranov.com/series/kill-the-hero/']
    def parse(self, response):
        title = response.css('div.post-title h1::text').get().strip()
        description = response.css('div.summary__content p::text').get()
        image_url = response.css('div.summary_image img::attr(src)').get()
        chapters = []
        yield {
            'title': title,
            'description': description,
            'image_url': image_url,
            'chapters': chapters
        }
        chapters_links = response.css('li.wp-manga-chapter a::attr(href)').getall()
        for chapter_link in chapters_links:
             yield response.follow(chapter_link, self.parse_chapter)
             
    def parse_chapter(self, response):
        chapter_title = response.css('h1#chapter-heading::text').get()
        images = response.css('img.wp-manga-chapter-img::attr(src)').getall()
        images = [img.strip() for img in images]
        yield {
            'chapter_title': chapter_title,
            'images': images
        }
