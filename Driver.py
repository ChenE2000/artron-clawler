from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    
    def login_auction(self) -> webdriver.Chrome:
        url = "https://passport.artron.net/login"
        self.driver.get(url)

        # find input
        username = self.driver.find_element(By.ID, "loginUsername")
        username.send_keys("17769334224")
        password = self.driver.find_element(By.ID, "loginPwd")
        password.send_keys("qwer4321")

        
        agreeBox = self.driver.find_element(By.CLASS_NAME, "agreeBox")
        # inner span
        agreeBox = agreeBox.find_element(By.TAG_NAME, "span")
        agreeBox.click()

        # find login button
        login_button = self.driver.find_element(By.ID, "memberLogin")
        login_button.click()

        # save cookies and keep waiting
        time.sleep(1)

        return self
    

    def get_auction_author_deal_info(self, aname: str) -> dict:
        
        driver = self.driver
        time.sleep(2)
        # selenium visit https://amma.artron.net/artronindex_artist.php
        driver.get("https://amma.artron.net/artronindex_artist.php")
        time.sleep(2)
        # find input
        input_bar = driver.find_element(By.ID, "artist")
        # input author name
        input_bar.send_keys(aname)
        time.sleep(2)

        # find search button
        search_button = driver.find_element(By.ID, "button2")
        # click search button
        search_button.click()
        
        # scroll down 50% of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        # ======================
        # find deal sum
        # ======================
        time.sleep(2)
        # find <a> with value 拍卖数据详情
        a = driver.find_element(By.LINK_TEXT, "拍卖数据详情")

        # click <a>
        a.click()
        time.sleep(2)
        # find <table class="detail-table"> 
        # table = driver.find_element(By.CLASS_NAME, "detail-table")
        table = driver.find_elements(By.CLASS_NAME, "charts")[2]
        # find <tbody>
        tbody = table.find_element(By.TAG_NAME, "tbody")
        # locate the last <tr> in <table>
        tr = tbody.find_elements(By.TAG_NAME, "tr")[-1]
        # extract 4 <td> in <tr>
        td = tr.find_elements(By.TAG_NAME, "td")

        # td[3].text消除千分位，去掉”万“

        # TODO formatting deal_sum
        return {
            "deal_sum": td[3].text,
            "deal_count": td[2].text,
            "total_auction": td[1].text,
            "dea_ratio": int(td[2].text) / int(td[1].text)
        } 
    
    def get_auction_work_info(self, wid: str):
        driver = self.driver
        time.sleep(2)
        url = f"https://auction.artron.net/paimai-art{wid}"
        driver.get(url)
        time.sleep(5)

        # find div with class="productDetailBox"
        div = driver.find_element(By.CLASS_NAME, "productDetailBox")
        # print(div.text)
        # find all dl in div
        dls = div.find_elements(By.TAG_NAME, "dl")
        print(dls)
        # get all dt and dd in dl
        work_info = {
            "拍品名称": None,
            "作者": None,
            "拍品分类": None,
            "创作年代": None,
            "尺寸": None,
            "估价": None,
            "成交价": None,
            "拍卖日期": None,
            "拍卖公司": None,
            "拍卖专场": None,
            "拍卖会": None,
            "材质": None,
            "形制": None,
            "题识": None,
            "著录": None
        }
        for dl in dls:
            dt = dl.find_element(By.TAG_NAME, "dt")
            dd = dl.find_element(By.TAG_NAME, "dd")
            work_info[dt.text] = dd.text
            # print("=====================================")

        return work_info


if __name__ == "__main__":
    driver = Driver()
    driver.login()