import time
from bs4 import BeautifulSoup
from WebBase import WebBase

class WebFedoraProject(WebBase):
    main_url="https://fedoraproject.org/start/"

    def parse_html(self):
        _ret = [ self.main_url  ]
        self._browser.get( self.main_url )
        time.sleep(15)
        html_content = self._browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        divs = soup.find_all('div',attrs={"data-v-debfea50":"","class":"animate-fade-in"})
        for div in divs:
            _ret.append( div.find('a')["href"] )
        return _ret
