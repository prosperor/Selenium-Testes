from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class CriarEnquete():

    driver = None
    link = str
    cabecalho = str

    def __init__(self) -> None:
        self.driver = Firefox() #Cria o self.driver que vai se comunicar com o firefox
        self.driver.get("https://www.strawpoll.me/") #Vai até o site descrito
        self.driver.maximize_window() #Maximiza a tela do navegador

    def preencher_e_criar_enquete(self,pergunta, opcoes: list):
        self.cabecalho = pergunta
        self.driver.find_element(By.CSS_SELECTOR, "#form-field-content-editable > div").send_keys(pergunta) #Escreve a pergunta
        # Escreve as opções
        self.driver.find_element(By.ID, "field-options-1-option").send_keys(opcoes.pop(0))
        ind = 2
        for opcao in opcoes:
            self.driver.find_element(By.NAME, f"options-option-{ind}").send_keys(opcao)
            ind += 1
        # Selecionar opção drop-down
        select = Select(self.driver.find_element(By.ID, "field-duplication-setting"))
        select.select_by_value("2")
        # Marcar as caixas (Checkbox)
        self.driver.find_element(By.ID, "field-require-recaptcha").click()
        self.driver.find_element(By.ID,"field-allow-multiple-choices").click()
        # Criar Enquete
        link = self.driver.current_url
        self.driver.find_element(By.ID, "create-button").click()
        # Salvar Link
        WebDriverWait(self.driver, 10).until(UrlHasChanged(link))
        self.link = self.driver.current_url
        #Fecha o navegador
        self.driver.close()
    
    def pegarLink(self):
        return self.link
    
    def pegarCabecalho(self):
        return self.cabecalho
    
class UrlHasChanged:
    def __init__(self, old_url):
        self.old_url = old_url

    def __call__(self, driver):
        return driver.current_url != self.old_url
    
    









 


