from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# selenium log level
selenium.webdriver.remote.remote_connection.LOGGER.setLevel(logging.WARNING)
class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    
    def login_auction(self):
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

    def download_auction_work_image(self, wid: str):
        driver = self.driver
        url = f"https://tulu.artron.net/wap/NewHdImage/bigpic/art{wid}"
        driver.get(url)
        time.sleep(5)

        # find <canvas>
        canvas = driver.find_element(By.TAG_NAME, "canvas")
        # save canvas as image
        canvas.screenshot(f"./images/{wid}.png")

    
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

    def get_art400_info(self) -> list:
        print("[LOGS] get art400 info")
        driver = self.driver
        time.sleep(2)
        url = "https://amma.artron.net/artronindex_indexall.php?cbid=1"
        driver.get(url)
        time.sleep(5)

        # find table with class="detail-table"
        table = driver.find_element(By.CLASS_NAME, "detail-table")
        tbody = table.find_element(By.TAG_NAME, "tbody")

        listArt400 = []
        # 保存表中2000年-2022共47条记录
        for trNum in range(47):
            art400_info = {
                "季度": None,
                "上拍数量": None,
                "成交数量": None,
                "成交额（万元）": None,
                "成交率": None,
                "指数": None
            }
            tr = tbody.find_elements(By.TAG_NAME, "tr")[trNum]
            td = tr.find_elements(By.TAG_NAME, "td")
            # 保存每条记录的6个字段
            # print(td[0].text)       #季度
            # print(td[1].text)       #上拍数量
            # print(td[2].text)       #成交数量
            # print(td[3].text)       #成交额
            # print(td[4].text)       #成交率
            # print(td[5].text)       #指数

            art400_info["季度"] = td[0].text
            art400_info["上拍数量"] = td[1].text
            art400_info["成交数量"] = td[2].text
            art400_info["成交额（万元）"] = td[3].text
            art400_info["成交率"] = td[4].text
            art400_info["指数"] = td[5].text
            listArt400.append(art400_info)

        return listArt400


    def get_art50_info(self):
        print("[LOGS] get art50 info")
        driver = self.driver
        time.sleep(2)
        url = "https://amma.artron.net/artronindex_exponent1.php?type=2"
        driver.get(url)
        time.sleep(5)

        table = driver.find_element(By.CLASS_NAME, "detail-table")
        tbody = table.find_element(By.TAG_NAME, "tbody")


        listArt50 = []

        # 保存表中2000年-2022年共45条记录
        for trNum in range(45):
            art50_info = {
                "季度": None,
                "重复交易数量": None,
                "指数": None,
            }
            tr = tbody.find_elements(By.TAG_NAME, "tr")[trNum]
            td = tr.find_elements(By.TAG_NAME, "td")
            # print(tr.text)
            # 保存每条记录的6个字段
            # print(td[0].text)  # 季度
            # print(td[1].text)  # 重复交易数量
            # print(td[2].text)  # 指数

            art50_info["季度"] = td[0].text
            art50_info["重复交易数量"] = td[0].text
            art50_info["指数"] = td[0].text

            listArt50.append(art50_info)

        return listArt50


if __name__ == "__main__":
    driver = Driver()
    driver.login()