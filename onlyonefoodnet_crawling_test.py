from selenium import webdriver
import config
browser = webdriver.Chrome("/Users/hyunsoojang/Downloads/chromedriver")
browser.implicitly_wait(5)

#온리원푸드넷 페이지 로드
browser.get('https://onlyonefoodnet.ifresh.co.kr/common/syscommon/authority/loginPage.fo')

#로그인 구현
browser.find_element_by_id('userId').send_keys(config.ONF_CONFIG.TEST_ID)
browser.find_element_by_id('passwd').send_keys(config.ONF_CONFIG.TEST_PWD)
browser.find_element_by_id('btnLogin').click()

#사용자전환 클릭
browser.find_element_by_xpath('//*[@id="headerMenu"]/div[1]/div[1]/a[4]').click()