#!/usr/bin/env python3

#WebActivity


from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



import schedule as global_scheduler
import logging
import time


from WebFedoraProject import WebFedoraProject
from WebWikipediaRussian import WebWikipediaRussian
from WebWikipediaEnglish import WebWikipediaEnglish
from WebHabr import WebHabr
from WebArxiv import WebArxiv


main_logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
    )

main_logger.info("запускаю основную программу")


main_logger.info("запускаю графический просмотр через браузер")
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-profile')
firefox_options.add_argument( '{}/.mozilla/firefox/WebActivity'.format(Path.home()) )
browser = webdriver.Firefox(firefox_options)
browser.get("https://www.mozilla.org/ru/")

web1 = WebFedoraProject(global_scheduler, main_logger, browser)
web1.set_schedule( "12:01", "14:40", 25 )

web2 = WebWikipediaRussian(global_scheduler, main_logger, browser)
web2.set_schedule( "10:00", "23:59", 35 )

web3 = WebWikipediaEnglish(global_scheduler, main_logger, browser)
web3.set_schedule( "09:05", "16:29", 45 )

web5 = WebArxiv(global_scheduler, main_logger, browser)
web5.set_schedule( "10:25", "23:00", 18 )

web4 = WebHabr(global_scheduler, main_logger, browser)
web4.set_schedule( "09:35", "16:00", 15 )


while True:
    global_scheduler.run_pending()
    time.sleep(60)
