import time
from bs4 import BeautifulSoup
from WebBase import WebBase

class WebDiscussionFedoraProject(WebBase):
    main_url="https://discussion.fedoraproject.org"

    def parse_html(self):
        _ret = [ self.main_url  ]
        self._browser.get( self.main_url + "/search?q=%20order%3Alatest_topic" )
        time.sleep(3)
        self._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self._browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        html_content = self._browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        divs = soup.find_all('div',attrs={"class":"topic"})
        for div in divs:
            _ret.append( self.main_url + div.find('a')["href"] )
        return _ret
