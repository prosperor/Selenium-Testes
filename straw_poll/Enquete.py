from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

class Enquete():

    driver = None
    cabecalho = str

    def __init__(self,link) -> None:
        self.driver = Firefox() #Cria o self.driver que vai se comunicar com o firefox
        self.driver.get(link) #Vai até o site descrito
        self.driver.maximize_window() #Maximiza a tela
        self.cabecalho = self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text
        
    def pegarCabecalho(self):
        return self.cabecalho
    
    


