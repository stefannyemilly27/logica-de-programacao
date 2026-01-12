# 5. Crie um programa que pergunte ao usuário uma senha e só saia do loop se ele digitar "1234".
while True:
    escolha = int(input("Digite sua senha de 4 dígitos: "))
    senha = 1234
    if escolha == senha:
        print("Acesso permitido!")
        break
    else:
        print("Acesso negado, tente novamente!")