from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

# ChromeDriverのパスを指定
chrome_driver_path = '/usr/local/bin/chromedriver'

# ChromeDriverの初期化（Serviceオブジェクトを使用）
service = ChromeService(executable_path=chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://sp.nogizaka46.com/'
browser.get(url)

# ボタンのクリック
elem_login_btn = browser.find_element(By.CLASS_NAME, "rounded")
elem_login_btn.click()

# メールアドレスでのログイン選択画面
sleep(2)
elem_mail_btn = browser.find_elements(By.CSS_SELECTOR, ".flex.w-full.items-center.justify-between.rounded-md.bg-blueGray-700.p-12.text-14.font-semibold.tracking-wider.text-white.mt-2")
elem_mail_btn[3].click()

# メールアドレス、パスワード入力画面
sleep(2)
browser.find_element(By.XPATH, "(//input[@type='email'])").send_keys("abcdefghijklmnopq")
browser.find_element(By.XPATH, "(//input[@type='password'])").send_keys("abcdefghijklmnopq")
elem_login2_btn = browser.find_element(By.CLASS_NAME, "css-y5yuzb")
elem_login2_btn.click()

#モバイル画面
sleep(2)
elem_live_btn = browser.find_elements(By.CSS_SELECTOR, ".flex.flex-grow")
elem_live_btn[1].click()

sleep(2)
#注意事項同意画面
elem_attention_btn = browser.find_elements(By.CSS_SELECTOR, ".checkbox.h-24.w-24")
elem_attention_btn[0].click()
sleep(2)
elem_attention_btn[1].click()
sleep(2)
elem_day_btn = browser.find_elements(By.CSS_SELECTOR, ".button-primary.mx-auto.min-w-240")
elem_day_btn[0].click()

#個人情報記入画面
sleep(3)
elem_credit_btn = browser.find_element(By.ID, 'radio2')
elem_credit_btn.click()
sleep(2)
elem_lastname_btn = browser.find_element(By.ID, 'last_name')
elem_lastname_btn.send_keys('月火水木君曜日金土日')
elem_firstname_btn = browser.find_element(By.ID, 'first_name')
elem_firstname_btn.send_keys('月火水木君曜日金土日')
elem_lastnamekana_btn = browser.find_element(By.ID, 'last_name_kana')
elem_lastnamekana_btn.send_keys('アイウエオアイウエオ')
elem_firstnamekana_btn = browser.find_element(By.ID, 'first_name_kana')
elem_firstnamekana_btn.send_keys('ガハハハハハハ')
elem_firstnamekana_btn = browser.find_element(By.ID, 'email_1')
elem_firstnamekana_btn.send_keys('kakikukekokakikukeko')
elem_firstnamekana_btn = browser.find_element(By.ID, 'email_1_confirm')
elem_firstnamekana_btn.send_keys('kakikukekokakikukeko')
elem_firstnamekana_btn = browser.find_element(By.ID, 'zip')
elem_firstnamekana_btn.send_keys('1000014')
elem_firstnamekana_btn = browser.find_element(By.ID, 'city')
elem_firstnamekana_btn.send_keys('千代田区')
elem_firstnamekana_btn = browser.find_element(By.ID, 'address_1')
elem_firstnamekana_btn.send_keys('永田町1-7-1')
elem_firstnamekana_btn = browser.find_element(By.ID, 'tel_1')
elem_firstnamekana_btn.send_keys('123456789')

elem_credit_btn = browser.find_element(By.ID, 'sex-sex-0')
elem_credit_btn.click()

elem_credit_btn = browser.find_element(By.ID, '申込時の注意事項等.0')
elem_credit_btn.click()
elem_firstnamekana_btn = browser.find_element(By.ID, '申込者名・姓(来場代表者苗字)')
elem_firstnamekana_btn.send_keys('月火水木君曜日金土日')
elem_firstnamekana_btn = browser.find_element(By.ID, '申込者名・名')
elem_firstnamekana_btn.send_keys('月火水木君曜日金土日')
elem_firstnamekana_btn = browser.find_element(By.ID, '申込者電話番号(半角・ハイフン不要)')
elem_firstnamekana_btn.send_keys('123456789')
elem_firstnamekana_btn = browser.find_element(By.ID, '同行者・姓')
elem_firstnamekana_btn.send_keys('あいうえおあいうえお')
elem_firstnamekana_btn = browser.find_element(By.ID, '同行者名・名')
elem_firstnamekana_btn.send_keys('あいうえおあいうえお')
elem_firstnamekana_btn = browser.find_element(By.ID, '同行者電話番号(半角・ハイフン不要)')
elem_firstnamekana_btn.send_keys('0123456789')
elem_firstnamekana_btn = browser.find_element(By.ID, '同行者住所')
elem_firstnamekana_btn.send_keys('あいうえおあいうえお')
elem_firstnamekana_btn = browser.find_element(By.ID, '同行者メールアドレス')
elem_firstnamekana_btn.send_keys('sinndokunattekita')
elem_credit_btn = browser.find_element(By.ID, '最終確認.0')
elem_credit_btn.click()

elem_firstnamekana_btn = browser.find_element(By.ID, 'review_password')
elem_firstnamekana_btn.send_keys('mazidezikannnomuda')

# 10分間待機
sleep(600)
