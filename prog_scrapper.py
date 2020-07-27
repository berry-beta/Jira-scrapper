from selenium import webdriver
from selenium.webdriver.common.keys import Keys

jira_path = "" #Past the path between the quotes " "

driver = webdriver.Chrome()
driver.get(jira_path) # Opening a new chrome window

progs = driver.find_elements_by_class_name("_3g3c2")

for prog in progs:
    nPrio = prog.find_element_by_class_name("_3pF1D")
    kProg = prog.find_element_by_class_name("_1-61V")
    print(nPrio.text + ";"+ kProg.text) #Displaying the feature infos and location in the backlog
   
