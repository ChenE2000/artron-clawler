from Driver import Driver
from Author import Author
from Work import Work

auction_driver = Driver().login_auction()


# i1 = driver.get_author_deal_info("徐悲鸿")
# i2 = driver.get_author_deal_info("齐白石")
works = [Work('5127381713'), Work('5127381714')]

for work in works:
    work_info = auction_driver.get_auction_work_info(work.wid)
    work.set_basic_info(work_info)
    work.save_to_json()

print(w1)