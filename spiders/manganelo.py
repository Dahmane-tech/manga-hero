import scrapy

class MangaSpider(scrapy.Spider):
    name = 'manga'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['manganelo.tv']
        self.start_urls = [start_url] if start_url else ['https://ww5.manganelo.tv/manga/manga-wh973642/']

    def parse(self, response):
        base_url ="https://ww5.manganelo.tv"
        title = response.css('div.story-info-right h1::text').get().strip()
        description =response.css('#panel-story-info-description ::text').getall()[2].strip()
        image_url = f'{base_url}{response.css("img.img-loading::attr(src)").get()}'

        chapter_links = [f'{base_url}{current_chapter}' for current_chapter in response.css('a.chapter-name::attr(href)').getall()]
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
        chapter_title = response.css('select.navi-change-chapter option[selected="selected"]::text').get().strip()

        # Extract the image URLs from the current page
        images = response.css('div.container-chapter-reader img.img-loading::attr(data-src)').getall()
        chapter ={
            
            'chapter_title': chapter_title,
            'images': images
        }
        return chapter
        
        
