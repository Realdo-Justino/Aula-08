#Sintaxe de função em python
def inicio():
    print("Oi")

inicio()

def teste(nome):
    print(nome)

teste("oi")

def teste2(*nome):
    print(nome[0],nome[1])

teste2("O","i")

def teste3(nome,idade,cpf):
    print(nome,idade,cpf)

teste3(nome="Realdo",idade=18,cpf=11111)

def teste4(**dados):
    print(dados["cpf"])

teste4(nome="Realdo",idade=18,cpf=11111)

def teste5(nome="Realdo"):
    print(nome)

teste5("O")

def teste6(lista):
    for i in lista:
        print(i)

minhaLista=["Realdo","Justino","Junior"]
teste6(minhaLista)

def teste7(lista):
    pass

def teste8(nome):
    if nome=="realdo":
        return True
    else:
        return False

print(teste8("realdo"))
variavel=teste8("realdo")

print(variavel)