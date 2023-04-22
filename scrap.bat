@echo off
del backup.json
set /p url=Enter URL To scrap: 

set supported_domains=mangalek.net arabshentai.com arabtoons.net ozulscans.com bibimanga.com kissmanga.org azoranov.com team1x1.fun manganelo.tv aresmanga.net
for %%d in (%supported_domains%) do (
  echo %url% | findstr /i "%%d" > nul
  if not errorlevel 1 (
    if "%%d"=="mangalek.net" (
      scrapy runspider "py.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="bibimanga.com" (
      scrapy runspider "bibimanga.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    ) else if "%%d"=="arabshentai.com" (
      scrapy runspider "hee.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="arabtoons.net" (
      scrapy runspider "hola.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="ozulscans.com" (
      scrapy runspider "ozulscans.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="azoranov.com" (
      scrapy runspider "azoranov.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="manganelo.com" (
      scrapy runspider "manganelo.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="aresmanga.net" (
      scrapy runspider "aresmanga.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="team1x1.fun" (
      scrapy runspider "team1x1.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )else if "%%d"=="kissmanga.org" (
      scrapy runspider "kissmanga.py" -a start_url=%url% -o output.json
	  python jso.py
      ren output.json backup.json
    )
    pause

    exit /b
  )
)

echo We don't support your domain
pause
