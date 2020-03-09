from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\AADI\\.wdm\\drivers\\chromedriver\\79.0.3945.36\\win32\\chromedriver.exe') 
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()
print("success click")

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
print("success")