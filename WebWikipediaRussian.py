import time
from bs4 import BeautifulSoup
from WebBase import WebBase

class WebWikipediaRussian(WebBase):
    main_url="https://ru.wikipedia.org/"

    def parse_html(self):
        _ret = [ self.main_url  ]
        self._browser.get( self.main_url )
        time.sleep(3)
        html_content = self._browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        divs = []
        divs.append(soup.find('div',attrs={"id":"main-cur", "class":"main-block main-box"}))
        divs.append(soup.find('div',attrs={"id":"main-dyk", "class":"main-block main-box"}))
        for div in divs:
            for li in div.find_all("li"):
                for b in li.find_all("b"):
                    for a in b.find_all("a"):
                        if a["href"].find("https://")>-1:
                            _ret.append( a["href"] )
                        else:
                            _ret.append( self.main_url + a["href"] )
        return _ret
