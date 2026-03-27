ler=input("qual ficheiro deseja ler")
with open(ler,"r", encoding="utf-8") as file3:
    funções=file3.readlines()
    for elemento_na_lista in funções:
        print (elemento_na_lista)
