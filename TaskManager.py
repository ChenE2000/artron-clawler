from Driver import Driver
from Author import Author
from Work import Work
import json
from tqdm import tqdm

if __name__ == "__main__":
    auction_driver = Driver().login_auction()

    auction_basic_info = {
        "auction_art400": auction_driver.get_art400_info(),
        "auction_art50": auction_driver.get_art50_info()
    }
    with open("./data/auction_basic_info.json", "w", encoding="utf-8") as f:
        json.dump(auction_basic_info, f, ensure_ascii=False)


    works = [Work('5127381713'), Work('5127381714')]
    authors = [Author('徐悲鸿'), Author('齐白石')]

    for author in tqdm(authors):
        author.get_author_id().get_life_span()
        deal_info = auction_driver.get_auction_author_deal_info(author.name)
        author.set_deal_info(deal_info)
        author.save_to_json()

    for work in tqdm(works):
        work_info = auction_driver.get_auction_work_info(work.wid)
        auction_driver.download_auction_work_image(work.wid)
        work.set_basic_info(work_info)
        work.save_to_json()
    
    print("Done!")