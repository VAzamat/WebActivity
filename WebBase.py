import logging
import time
import random
from datetime import datetime, time as dt_time

class WebBase():
    main_url="https://ru.wikipedia.org/"
    def __init__(self, global_scheduler, logger, browser):
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.global_scheduler = global_scheduler
        self._from_time = datetime.strptime("00:01", "%H:%M").time()
        self._logger.info(f"Расписание по умолчанию с {self._from_time}")
        self._browser = browser
        self._html_urls = []
        self.get_html_urls() #get links at start of program

    def set_schedule(self, from_time = "00:01", to_time= "23:59", interval_minutes=1 ):
        self._logger.info(f"Устанавливаю расписание")
        self._logger.info(f"Запуск get_html_urls ежедневно в {from_time}")
        self.global_scheduler.every().day.at( from_time ).do( self.get_html_urls )
        self._from_time = datetime.strptime(from_time, "%H:%M").time()
        self._logger.info(f"Запуск fake_load_webpage каждые {interval_minutes} минут с {self._from_time} до {to_time}")
        self.global_scheduler.every(interval_minutes).minutes.until(to_time).do( self.fake_load_webpage )

    def get_html_urls(self):
        #скачать main_url через browser и вернуть список в self._html_urls
        self._logger.info(f"Смотрю главную страницу, собираю ссылки")
        try:
            self._html_urls = self.parse_html()
        except:
            self._html_urls = [ self.main_url ]
        self._logger.info(f"{self._html_urls}")

    def fake_load_webpage(self):
        now = datetime.now().time()
        if now<self._from_time:
            return
        delay = random.randint(10,25)
        time.sleep(delay)
        url = random.choice (self._html_urls)
        self._logger.info(f"Смотрю страницу в интернете по ссылке {url}")
        try:
            self._browser.get( url )
        except:
            self._logger.info(f"Проблемы с интернетом")

    def parse_html(self):
        _ret = []
        return _ret
