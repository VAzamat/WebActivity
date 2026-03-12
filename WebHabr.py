import time
from bs4 import BeautifulSoup
from WebBase import WebBase

#https://habr.com/ru/feed/
#https://habr.com/en/feed/

class WebHabr(WebBase):
    main_url="https://habr.com"

    def parse_html(self):

        _ret = [ self.main_url  ]
        urls = [ self.main_url + "/ru/feed/", self.main_url+"/ru/feed/page2", self.main_url+"/ru/feed/page3/"]
        urls = [ self.main_url + "/en/feed/", self.main_url+"/en/feed/page2", self.main_url+"/en/feed/page3/"]
        for url in urls:
            self._browser.get( url )
            time.sleep(15)
            html_content = self._browser.page_source

            soup = BeautifulSoup(html_content, 'html.parser')
            for a in soup.find_all("a",attrs={"class":"tm-title__link", "data-article-link":"true", "data-test-id":"article-snippet-title-link"}):  #для английской
            #for a in soup.find_all("a",attrs={"class":"tm-article-datetime-published tm-article-datetime-published_link"}):  #для русской
                if a["href"].find("/articles/")>-1:
                    if a["href"].find("https://")>-1:
                        _ret.append( a["href"] )
                    else:
                        _ret.append( self.main_url + a["href"] )


        return _ret
