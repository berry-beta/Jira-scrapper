# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://jira.antai.gouv.fr/secure/PortfolioPlanView.jspa?id=12&sid=12#plan/backlog") # ouverture d'une fenêtre Chrome et accès à Jira
           # A l'ouverture il faut :
           # 1- se logger sur Jira
           # 2- régler les filtres (Epic to Epic; PI2 etc.)
           # 3- dezoommer pour que toutes les lignes s'affichent à l'écran
input() # une fois la préparation terminée; entrez une lettre dans la console pour reprendre l'execution
print("ok")
progs = driver.find_elements_by_class_name("_3g3c2")

for prog in progs:
    nPrio = prog.find_element_by_class_name("_3pF1D")
    kProg = prog.find_element_by_class_name("_1-61V")
    print(nPrio.text + ";"+ kProg.text)
   #toutes les prio et les progs sont affichées dans la console prêtes à être copiées collées
