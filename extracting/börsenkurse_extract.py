from selenium import webdriver
import time
import random

def randomtime:
  time.sleep(random.randint(2, 5))

driver = webdriver.Firefox(executable_path=r'C:/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://world-hack.org')
driver.switch_to.frame("//frameset/frame")

driver.find_element_by_name('nick').send_keys('hackerfrosch')
randomtime()
driver.find_element_by_name('password').send_keys('passwort')
randomtime()
driver.find_element_by_xpath("//input[@value='   Login   ']").submit()
randomtime()

link_cluster = driver.find_element_by_link_text('Cluster').click()
randomtime()
link_finanzen = driver.find_element_by_link_text('Finanzen').click()
randomtime()
link_clusterbörse = driver.find_element_by_link_text('Clusterbörse').click
randomtime()

aktien = []
aktie_hax = driver.find_element_by_xpath("//[@width='70%']/b").text
aktien_append(aktie_hax)
print (aktien)
driver.quit()
