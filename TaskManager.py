from Driver import Driver

driver = Driver().login()
i1 = driver.get_deal_info("徐悲鸿")
i2 = driver.get_deal_info("齐白石")

print(i1, i2)