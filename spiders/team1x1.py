import scrapy
class MySpider(scrapy.Spider):
    name = 'team1x1.fun'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['team1x1.fun']
        self.start_urls = [start_url] if start_url else ['https://team1x1.fun/series/release-that-witch']
    def parse(self, response):
        title = response.css('div.author-info-title h1::text').get().strip()
        description = response.css("div.review-content p::text").get()
        image_url = response.css("img[alt='Manga Image']::attr(src)").get()
        chapters = []
        yield {
            'title': title,
            'description': description,
            'image_url': image_url,
            'chapters': chapters
        }
        tables_links =response.css('li.page-item a::attr(href)').getall()
        tables_links.append(self.start_urls[0])
        if (tables_links):
            for table_link in tables_links:
                yield response.follow(table_link, self.parse_table)
        else:
            chapters_links = response.css('div.eplisterfull li a::attr(href)').getall()
            for chapter_link in chapters_links:
                yield response.follow(chapter_link, self.parse_chapter)
            

    def parse_table(self, response):
        for chapter_link in response.css('div.eplisterfull li a::attr(href)').getall():
            yield response.follow(chapter_link, self.parse_chapter)

    def parse_chapter(self, response):
        chapter_title = response.css('h1#chapter-heading::text').get()
        images = response.css('div.image_list div.page-break img::attr(src)').getall()
        yield {
            'chapter_title': chapter_title,
            'images': images
        }
