import requests
import re
from Driver import Driver
from selenium.webdriver.common.by import By

from  bs4 import  BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

class Author:

    def __init__(self, name: str):
        self.session = requests.session()
        self.name = name
        self.author_id = None
        self.driver = driver
    
    
    def get_popularity(self):
        pass

    def get_author_id(self):
        url = f"https://artso.artron.net/artist/search_artist.php?keyword={self.name}"
        print(url)
        response = self.session.get(url, headers=headers)
        # 找到class="more"的a标签
        soup = BeautifulSoup(response.text, "html.parser")
        a = soup.find("a", class_="more")
        # 获取a标签的href属性
        href = a["href"]
        # 获取作者的id
        self.author_id = re.findall(r"\d+", href)[0]
        return self
    
    def get_life_span(self):
        url = f"https://artso.artron.net/artist/search_artist.php?keyword={self.name}"
        print(url)
        
        response = self.session.get(url, headers=headers)

        # 找到class="baseInfo"的div标签
        soup = BeautifulSoup(response.text, "html.parser")
        dl = soup.find("dl", class_="fix")
        # dl -> dd -> p
        p = dl.find("dd").find("p")
        # p的内容
        content = p.text
        # encoding
        content = content.encode("iso-8859-1").decode("utf-8")
        # 获取（）中的内容
        life_span = re.findall(r"（(.*)）", content)[0]
        # print(life_span)
        self.life_span = life_span
        return self



        
if __name__ == "__main__":
    driver = Driver()
    
    author = Author("徐悲鸿")
