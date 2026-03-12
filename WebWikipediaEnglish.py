import time
from bs4 import BeautifulSoup
from WebBase import WebBase

class WebWikipediaEnglish(WebBase):
    main_url="https://en.wikipedia.org/"

    def parse_html(self):
        _ret = [ self.main_url  ]
        self._browser.get( self.main_url )
        time.sleep(3)
        html_content = self._browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        divs = []
        divs.append(soup.find('div',attrs={"id":"mp-dyk", "class":"mp-contains-float"}))
        divs.append(soup.find('div',attrs={"id":"mp-otd", "class":"mp-contains-float"}))
        divs.append(soup.find('div',attrs={"id":"mp-right", "class":"MainPageBG mp-box"}))
        for div in divs:
            for li in div.find_all("li"):
                for b in li.find_all("b"):
                    for a in b.find_all("a"):
                        if a["href"].find("https://")>-1:
                            _ret.append( a["href"] )
                        else:
                            _ret.append( self.main_url + a["href"] )
        return _ret
