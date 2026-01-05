from funcoes import*
biblioteca = []
opcao = input(
"Escolha uma opção da biblioteca: 1 - Adicionar livro, 2 - Exibir todos os livros, 3 - Emprestar livro, 4 - Devolver livro, 0 - Sair  "
)

if opcao == 1:
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    livro = {
    "Título": titulo,
    "Autor": autor,
    "Status": "Disponível",
}
    biblioteca.append(livro)
    print("Livro adicionado com sucesso!")