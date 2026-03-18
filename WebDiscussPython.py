import time
from bs4 import BeautifulSoup
from WebBase import WebBase

class WebDiscussPython(WebBase):
    main_url="https://discuss.python.org"

    def parse_html(self):
        _ret = [ self.main_url  ]
        self._browser.get( self.main_url + "/latest" )
        time.sleep(3)
        self._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        html_content = self._browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        tds = soup.find_all('td',attrs={"class":"main-link topic-list-data"})
        for td in tds:
            _ret.append( self.main_url + td.find('a')["href"] )
        return _ret
