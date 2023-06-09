# manga-hero
A manga web page based on Scrapy spiders that make it more flexible and simple

[![MIT license](https://img.shields.io/badge/license-MIT-green "MIT license")](./LICENSE.md "MIT license") [![Scrapy Spider](https://img.shields.io/badge/-scrapy-3A9E9E "Scrapy Spider")](https://scrapy.org/ "scrapy spider") [![Manga Hero](https://img.shields.io/static/v1?label=Web%20site&message=manga-hero&color=3A9E9F "Manga Hero")](https://dahbot.000webhostapp.com/manga_hero/ "Manga Hero")

![scraped manga](https://img.shields.io/badge/dynamic/json?label=total-scraped-manga&query=$[%27total-scraped-manga%27]&url=https://api.jsonbin.io/v3/b/6443efbd9d312622a34fd4da/latest?meta=false "scraped manga") ![available domains to scrap](https://img.shields.io/badge/dynamic/json?label=domains-count-available-to-scrap&query=$[%27total-domains-available-to-scrap%27]&url=https://api.jsonbin.io/v3/b/6443efbd9d312622a34fd4da/latest?meta=false "available domains to scrap")
 ## Features
- [x] Easy-to-use Scrapy spiders for scraping manga web pages.
- [x] Flexible and customizable to suit different manga sources.
- [x] No central management, allowing anyone to add a manga as they wish.
- [x] Scrapes a large number of manga titles.
- [x] Supports multiple domains for scraping.
- [x] Provides dynamic badges to display scraped manga count and available domains count.
- [x] MIT license for open-source usage.
- [x] Integrates with Manga Hero website for easy access to manga content.
- [x] Regular updates and improvements for better performance.
- [x] ad-free.

## to do 
- [ ] Background keyframe bookmarking for chapters,
- [ ] allowing users to easily mark their progress and share it with others (requires login).
- [ ] Page count feature to keep track of the total number of pages in a manga.
- [ ] Cookie-based reading progress saving and restoration for convenient reading across sessions.
- [ ] Lock feature for horizontal and vertical scroll on Android devices for enhanced reading experience.
- [ ] Rapid chapters menu for quick navigation to specific chapters.
- [ ] Jump-to-page method allowing users to directly go to a specific page number.
- [ ] Editable restore zoom button for fitting content to maximum or minimum display.
- [x] Download button for each chapter as a ZIP file for offline reading.
- [ ] Footer with the author's name for personal branding.
- [ ] Split button in continuous view mode, separating images into two parts and doubling the page count.
- [ ] Customizable theme options, including background image and color settings.
- [ ] Chat room feature for each chapter (requires login) for interactive discussions.
- [ ] Support for two viewing modes: continuous scrolling and single-page view.
- [x] MIT license for open-source usage, ensuring compliance with open-source standards.
## supported domains
|                    SITE                    |   NATIVE LANGUAGE  |   STATUS    |
|:------------------------------------------:|:------------------:|:-----------:|
|     [azoranov](https://azoranov.com/)      |       ARABIC       |   PERFECT   |
| [aresmanga](https://aresmanga.net/series/) |       ARABIC       |   PERFECT   |
|.    [mangalek](https://mangalek.net)       |       ARABIC       |   PERFECT   |
| [ozulscans](https://ozulscans.com/manga/)  |       ARABIC       |   PERFECT   |
|     [team1x1](https://team1x1.fun)         |       ARABIC       |   PERFECT   |
|     [kissmanga](https://kissmanga.org/)    |       ENGLISH      |   PERFECT   |
|     [bibimanga](https://bibimanga.com/)    |       ENGLISH      |   MEDIUM    |
|     [manganelo](https://ww5.manganelo.tv/) |       ENGLISH      |   PERFECT   |
## requidment of adding new manga to our website.
- scrapy framework 
### instalation 
- you can install Scrapy using the Python package manager, pip. Open a command prompt or terminal window and run the following command
--`pip install scrapy` 
## adding new files to our-website 
 1. Download this  repository from this [link](https://github.com/Dahmane-tech/manga-hero/archive/refs/heads/main.zip).
 2. Visit one of the supported domains.
 3. Search for your manga and go to its main page where you can find the description and chapters.
 4. Copy the URL of the manga's main page.
 5. Run the scrap.bat file on your Windows machine.
 6. Paste the copied link when prompted.
 7. That's it! The scraping process will start automatically.
### example of main page of manga
-one piece
 --`https://kissmanga.org/manga/manga-aa951409`
