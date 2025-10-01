# Definir estoque 
while True:
    try:
        Estoque = int(input("Defina o estoque inicial: "))
        if Estoque > 0:
            break
        else:
            print("O estoque deve ser maior que zero.")
    except ValueError:
        print("Por favor, digite um número válido.")


limite_amarelo = Estoque * 0.50   
limite_vermelho = Estoque * 0.15 

while True:
    try:
        print("\nSeja Bem-Vindo ao IM-date")
        Saida = int(input("Quantidade de peças retiradas: "))  

        Estoque -= Saida  

      
        if Estoque >= limite_amarelo:
            print("✅ Luz Verde")
        elif Estoque >= limite_vermelho:
            print("⚠️ Luz Amarela")
        else:
            print("🔴 Luz Vermelha")

        print("Peças restantes:", Estoque)

        if Estoque <= 0:
            print("🔴 Estoque esgotado!")
            break  

    except ValueError:
        print("Por favor, digite um número válido.")

