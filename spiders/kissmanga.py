import scrapy
import re
class MangaSpider(scrapy.Spider):
    name = 'manga'
    def __init__(self, start_url=None, *args, **kwargs):
        super(MangaSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['kissmanga.org']#//*//
        self.start_urls = [start_url] if start_url else ['https://kissmanga.org/manga/manga-ah978064']#//*//

    def parse(self, response):
        title = response.css('h2 strong.bigChar::text').get().strip()#//*//
        processed_string = ''.join(c for c in title if c.isalpha())  
        title = ' '.join(w.capitalize() for w in processed_string.split())
        description = response.css("div.summary p::text").get().strip()#//*//
        image_url = response.css("meta[property='og:image']::attr(content)").get()#//*//
        base_url = 'https://kissmanga.org/'
        
        chapters_links = response.css('div.listing.full div div h3 a::attr(href)').getall()#//*//
        full_chapters_links = [base_url + url for url in chapters_links]
        chapters = []
        for chapter_link in full_chapters_links:
            chapter =  yield scrapy.Request(chapter_link, callback=self.parse_chapter)
            
        yield {
            'title': title,
            'description': description,
            'image_url': image_url,
            'chapters': chapters
            
        }
        yield{chapter}

    def parse_chapter(self, response):
        title = response.meta.get('title')

        # Extract the chapter title
        chapter_title   =re.search(r'Chapter (\d+)', response.css('meta[property="og:title"]::attr(content)').get()).group(0)

        # Extract the image URLs from the current page
        images = response.css('div#centerDivVideo img::attr(src)').getall()#//*//
        images = [img.strip() for img in images]
        chapter ={
            
            'chapter_title': chapter_title,
            'images': images
        }
        return chapter