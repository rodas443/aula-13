with open("file_with_three_line.txt","r", encoding="utf-8") as file3:
    linha10= file3.read(10)
    print (linha10)

    linha11 = file3.read(11)
    print (linha11)

    linha12 = file3.read(12)
    print (linha12)




with open("file_with_three_line.txt","r", encoding="utf-8") as file3:
    todas= file3.readlines()
    print (todas)
    contagem=0
    for linha in todas:
        contagem=contagem+1
        if contagem== 10 or contagem==11 or contagem==12:
            print (linha)