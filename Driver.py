from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    
    def login(self) -> webdriver.Chrome:
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
    

    def get_deal_info(self, aname: str):
        
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

        
        return {
            "deal_sum": td[3].text,
            "deal_count": td[2].text,
            "total_auction": td[1].text,
            "dea_ratio": int(td[2].text) / int(td[1].text)
        } 
    


if __name__ == "__main__":
    driver = Driver()
    driver.login()