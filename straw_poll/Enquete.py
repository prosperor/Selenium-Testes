from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from pathlib import Path

class Enquete():

    def pegarCabecalho(link):
        
        driver = Firefox(executable_path=Path("Straw_Poll", "geckodriver.exe")) #Cria o self.driver que vai se comunicar com o firefox
        driver.get(link) #Vai até o site descrito
        driver.maximize_window() #Maximiza a tela
        cabecalho = driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text
        driver.close()
        return cabecalho
        
        
    
    


