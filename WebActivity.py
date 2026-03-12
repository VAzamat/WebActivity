#!/usr/bin/env python3


from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



import schedule as global_scheduler
import logging
import time

from WebFedoraProject import WebFedoraProject


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

while True:
    global_scheduler.run_pending()
    time.sleep(60)
