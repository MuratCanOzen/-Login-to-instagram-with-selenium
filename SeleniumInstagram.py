from selenium import webdriver
import time

browser=webdriver.Chrome(executable_path="C:\seleniumbrowserdriverSave\chromedriver.exe")
browser.get("https://www.instagram.com")
time.sleep(5)
# Bu kısımda webdriver olarak chrome kullanılarak instagram adresine gidilir.

# //*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a
# giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[2]/p/a")
# giris_yap.click()
# time.sleep(3)

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")
username.send_keys("*****") # Bu aşamada kullanıcı adının verlmiş olması gerekir.
password.send_keys("*****") # Bu aşamada şifrennin verilmiş olması gerekir.

time.sleep(5)

login=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
login.click()
 # Bu kısımda önceki aşamada girilen kullanıcı adı ve şifre kullanılarak otomatik şekilde
 # login butonuna tıklama işlemi yapılır.

time.sleep(5)

react=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/section/div/button")
react.click()
# Bu kısımda karşımıza çıkan sekmenin onayı verilir ve sekme kapatılır.
time.sleep(10)
browser.close()
# Bu kısımda ise 10 saniye bekleme süresinden sonra instagram sekmesi kapatılır.