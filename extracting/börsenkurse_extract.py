from selenium import webdriver
import time
import random


def randomtime():
    time.sleep(random.randint(2, 5))


driver = webdriver.Firefox(executable_path=r'C:/Users/nikan/Desktop/who-analytics/python/geckodriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://world-hack.org')

iframe = driver.find_element_by_xpath("//frameset/frame")
driver.switch_to.frame(iframe)

login_name = driver.find_element_by_name('nick')
login_password = driver.find_element_by_name('password')
login_submit = driver.find_element_by_xpath("//input[@value='  Login  ']")

randomtime()
login_name.send_keys('hackerfrosch')
randomtime()
login_password.send_keys('timmi77')
randomtime()
login_submit.submit()
randomtime()

link_cluster = driver.find_element_by_link_text('Cluster').click()
randomtime()
link_cluster_finanzen = driver.find_element_by_link_text('Finanzen').click()
randomtime()
link_cluster_finanzen_clusterbörse = driver.find_element_by_link_text('Clusterbörse').click()
randomtime()

ak_hax = driver.find_element_by_xpath("//td[@width='70%']/b").text
ak_admin = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[2]/td[2]").text.replace(" Credits/Aktie", "")
ak_ibm = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[3]/td[2]").text.replace(" Credits/Aktie", "")
ak_bo = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[4]/td[2]").text.replace(" Credits/Aktie", "")
ak_vkh = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[5]/td[2]").text.replace(" Credits/Aktie", "")
ak_god = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[6]/td[2]").text.replace(" Credits/Aktie", "")
ak_f7 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[7]/td[2]").text.replace(" Credits/Aktie", "")
ak_sbh = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[8]/td[2]").text.replace(" Credits/Aktie", "")
ak_s8 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[9]/td[2]").text.replace(" Credits/Aktie", "")
ak_tnw = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[10]/td[2]").text.replace(" Credits/Aktie", "")
ak_dbh = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[11]/td[2]").text.replace(" Credits/Aktie", "")
ak_s9 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[12]/td[2]").text.replace(" Credits/Aktie", "")
ak_smf = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[13]/td[2]").text.replace(" Credits/Aktie", "")
ak_uof = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[14]/td[2]").text.replace(" Credits/Aktie", "")
ak_tdf1 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[15]/td[2]").text.replace(" Credits/Aktie", "")
ak_nds = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[16]/td[2]").text.replace(" Credits/Aktie", "")
ak_afd = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[17]/td[2]").text.replace(" Credits/Aktie", "")
ak_mms = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[18]/td[2]").text.replace(" Credits/Aktie", "")
ak_cds = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[19]/td[2]").text.replace(" Credits/Aktie", "")
ak_j4f = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[20]/td[2]").text.replace(" Credits/Aktie", "")
ak_it = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[21]/td[2]").text.replace(" Credits/Aktie", "")
ak_nfu = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[22]/td[2]").text.replace(" Credits/Aktie", "")
ak_f7e1 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[23]/td[2]").text.replace(" Credits/Aktie", "")
ak_v1ru5 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[24]/td[2]").text.replace(" Credits/Aktie", "")
ak_f7e2 = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[25]/td[2]").text.replace(" Credits/Aktie", "")
ak_sxx = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[26]/td[2]").text.replace(" Credits/Aktie", "")
ak_woc = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[27]/td[2]").text.replace(" Credits/Aktie", "")
ak_ibmh = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[28]/td[2]").text.replace(" Credits/Aktie", "")
ak_urp = driver.find_element_by_xpath("//td[@width='70%']/table/tbody/tr[29]/td[2]").text.replace(" Credits/Aktie", "")

aktien = [ak_hax, ak_admin, ak_ibm, ak_bo, ak_vkh, ak_god, ak_f7, ak_sbh, ak_s8, ak_tnw, ak_dbh, ak_s9, ak_smf, ak_uof, ak_tdf1, ak_nds, ak_afd, ak_mms, ak_cds, ak_j4f, ak_it, ak_nfu, ak_f7e1, ak_v1ru5, ak_f7e2, ak_sxx, ak_woc, ak_ibmh, ak_urp]

print(aktien)
