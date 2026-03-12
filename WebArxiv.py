import time
from bs4 import BeautifulSoup
from WebBase import WebBase



class WebArxiv(WebBase):
    main_url="https://arxiv.org/list/astro-ph/recent?skip=0&show=250"
    main_short="https://arxiv.org"

    def parse_html(self):
        _ret = [ self.main_url  ]
        self._browser.get( self.main_url )
        time.sleep(3)
        html_content = self._browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        a_tags = []
        a_tags += soup.find_all('a',attrs={"title":"Download PDF"})
        a_tags += soup.find_all('a',attrs={"title":"View HTML"})
        a_tags += soup.find_all('a',attrs={"title":"Abstract"})
        a_tags += soup.find_all('a',attrs={"title":"Download PDF"})
        for a in a_tags:
            if a["href"].find("https://")>-1:
                _ret.append( a["href"] )
            else:
                _ret.append( f"{self.main_short}{a["href"]}".replace("//","/") )
        return _ret
