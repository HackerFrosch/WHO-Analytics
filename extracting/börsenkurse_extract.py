from selenium import webdriver
import random
import time


def randomtime(t1, t2):
    time.sleep(random.randint(t1, t2))


def autologin(name, password):
    login_name = driver.find_element_by_name('nick')
    login_password = driver.find_element_by_name('password')
    login_submit = driver.find_element_by_xpath("//input[@value='  Login  ']")
    randomtime(2, 5)
    login_name.send_keys(name)
    randomtime(2, 5)
    login_password.send_keys(password)
    randomtime(2, 5)
    login_submit.submit()
    randomtime(2, 5)


def selectbörse():
    driver.find_element_by_link_text('Cluster').click()
    randomtime(2, 5)
    driver.find_element_by_link_text('Finanzen').click()
    randomtime(2, 5)
    driver.find_element_by_link_text('Clusterbörse').click()
    randomtime(2, 5)


driver = webdriver.Firefox(executable_path=r'C:/Users/v.masuch/Desktop/who-analytics/extracting/geckodriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://world-hack.org')

iframe = driver.find_element_by_xpath("//frameset/frame")
driver.switch_to.frame(iframe)

name = "hackerfrosch"
password = ""
autologin(name, password)

selectbörse()

aktien = []
ak_hax = driver.find_element_by_xpath("//td[@width='70%']/b").text
aktien.append(ak_hax)

schleife = 0

while schleife == 0:
    for var in range(2, 29):
        ak = driver.find_element_by_xpath(f"//td[@width='70%']/table/tbody/tr[{var}]/td[2]").text.replace(" Credits/Aktie", "")
        aktien.append(ak)

    print(aktien)
    time.sleep(900)
    print("+15 Minuten")
    selectbörse()
    time.sleep(900)
    print("+30 Minuten")
    selectbörse()
    time.sleep(900)
    print("+45 Minuten")
    selectbörse()
    time.sleep(900)
    print("+60 Minuten")
    selectbörse()
