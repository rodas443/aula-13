def cria_um_ficheiro():
    nome=input("Digite o nome do ficheiro? ")
    with open(nome, "w",encoding="utf-8") as file2:
        print("O ficheiro foi criado com sucesso.")
        frase=input("Digite a frase que deseja inserir: ")
        file2.write(frase)
        print("A frase foi adicionada no ficheiro com sucesso.")

def Inserir_frase():
    ficheiro=input("Qual frase deseja inserir no ficheiro com nome- file_with_one_line.txt? ")
    with open("file_with_one_line.txt", "a", encoding="utf-8") as file2:
        file2.write(ficheiro)

resposta=input("Deseja criar um ficheiro ou Inserir um frase")

if resposta == "Criar um ficheiro" or resposta == "criar um ficheiro":
    cria_um_ficheiro()
elif resposta== "Inserir uma frase" or resposta== "inserir um ficheiro":
    Inserir_frase()
else:
    print("Tens de escolher uma opção válida")