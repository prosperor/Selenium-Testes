from CriarEnquete import CriarEnquete
from Enquete import Enquete

def enqueteFeita(cabecalho,cabecalho_2):
    return (cabecalho == cabecalho_2)
    
pergunta, opcoes = ["Qual plataforma você prefere?",["DOOM Eternal (id software/Bethesda)", "Final Fantasy VII Remake (Square Enix)", "Ghost of Tsushima (Sucker Punch/SIE)", "Hades (Supergiant Games)", "The Last of Us Part II (Naughty Dog/SIE)"]]
    
cEnquete = CriarEnquete()
cEnquete.preencher_e_criar_enquete(pergunta,opcoes)
link = cEnquete.pegarLink()
eCabecalho = Enquete.pegarCabecalho(link)
    
    ###Testes
    
if (cEnquete.pegarCabecalho() == eCabecalho):
    print("Teste passou!!! O formulário foi criado com sucesso!")
else:
    print(f"Pergunta digitada = {cEnquete.pegarCabecalho()}")
    print(f"Retorno = {eCabecalho}")
    print("Erro, formulário não criado corretamente")
    
    

    






