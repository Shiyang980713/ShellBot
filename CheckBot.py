from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract
from time import sleep
from PIL import Image

#学号
your_id = ""
#密码
your_passwd = ""

try:
    driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range = 3).install())
except :
    #bot.send_message(tg_chat_id, "retry connect")
    sleep(100)
    driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range = 3).install())

driver.get("https://zlapp.fudan.edu.cn/site/ncovfudan/daily")

#LoginPageVariable
sleep(5)
my_id = driver.find_element_by_xpath('//*[@id="username"]')
my_passwd = driver.find_element_by_css_selector('#password')
button_login = driver.find_element_by_xpath('//*[@id="idcheckloginbtn"]')

#Login
my_id.clear()
my_passwd.clear()

my_id.send_keys(your_id)
my_passwd.send_keys(your_passwd)

button_login.click()

sleep(5)

#处理弹窗
try:
    Known = driver.find_element_by_css_selector('#wapat > div > div.wapat-btn-box > div')
    Known.click()
except :
    pass
    #bot.send_message("", "无弹窗 非首次登陆")

sleep(3)

#CheckId
id_png = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/section/div[4]/ul/li[3]/div/input")
id_png.screenshot('my_id.png')
getted_id = pytesseract.image_to_string(Image.open('my_id.png'))
if your_id in getted_id:
    pass
    #bot.send_message("", "IdCheck")
else:
    pass
    #bot.send_message("", "IdWrong")

#FillInLocation
location = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/section/div[4]/ul/li[6]/div/input")
location.click()

sleep(3)


sleep(3)


#Submit
submit = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/section/div[5]/div/a/em")
submit.click()

#MakeSure
try:
    sure = driver.find_element_by_css_selector('#wapcf > div > div.wapcf-btn-box > div.wapcf-btn.wapcf-btn-ok')
    sure.click()
except:
    pass
    #bot.send_message("", "You have submitted today")

sleep(3)

driver.quit()