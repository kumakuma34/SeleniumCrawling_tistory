from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import config
import time
driver = webdriver.Chrome("/Users/hyunsoojang/Downloads/chromedriver")
driver.implicitly_wait(5)

def check_exist_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exist_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True


#온리원푸드넷 페이지 로드
driver.get('https://onlyonefoodnet.ifresh.co.kr/common/syscommon/authority/loginPage.fo')

#로그인 가능여부 점검
driver.find_element_by_id('userId').send_keys(config.ONF_CONFIG.TEST_ID)
driver.find_element_by_id('passwd').send_keys(config.ONF_CONFIG.TEST_PWD)
driver.find_element_by_id('btnLogin').click()

login_success = check_exist_by_xpath('//*[@id="headerMenu"]/div[1]/div[1]/span[1]')
print('로그인 성공 여부 : ' + str(login_success))

#사용자전환 클릭
driver.find_element_by_xpath('//*[@id="headerMenu"]/div[1]/div[1]/a[4]').click()
change_account_search = driver.find_element_by_id('POP_USER_CHANGE_SEARCH_VAL')
change_account_search.send_keys(config.ONF_CONFIG.KIDS_ACCOUNT)
change_account_search.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_id('pop_userChange_btnChoice').click()

#iframe 전환
time.sleep(3)
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

#결제예상금액 조회 - PI 통
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mainSttlSearchBtn"]').send_keys(Keys.ENTER)
pi_success = check_exist_by_id('sttlScdAt')
pi_element = driver.find_element_by_id('sttlScdAt')
print(str(pi_success))
print(pi_element.text)


