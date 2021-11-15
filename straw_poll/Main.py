from CriarEnquete import CriarEnquete
from Enquete import Enquete

def enqueteFeita(cabecalho,cabecalho_2):
    return (cabecalho == cabecalho_2)

def montarCabecalho():
    pergunta = input("Qual pergunta você deseja fazer? ")
    opcoes = [input("Digite a primeira opção "),input("Digite a segunda opção ")]
    opcao = str()

    while(opcao != "."):
        opcao = input("Digite a próxima opção, ou digite '.' (sem as aspas) caso já tenha inserido as opções que deseja ")
        if opcao != ".":
            opcoes.append(opcao)
    
    return (pergunta,opcoes)


if __name__ == "__main__":
    
    pergunta, opcoes = ["Qual seu nome?",["Mario","Fernanda","Rayssa"]]
    
    cEnquete = CriarEnquete()
    cEnquete.preencher_e_criar_enquete(pergunta,opcoes)
    link = cEnquete.pegarLink()
    
    enquete = Enquete(link)
    
    ###Testes
    
    if (cEnquete.pegarCabecalho() == enquete.pegarCabecalho()):
        print("Teste passou, o formulário foi criado com sucesso")
    else:
        print(f"Pergunta digitada = {cEnquete.pegarCabecalho()}")
        print(f"Retorno = {enquete.pegarCabecalho()}")
        print("Erro, formulário não criado corretamente")
    
    

    






