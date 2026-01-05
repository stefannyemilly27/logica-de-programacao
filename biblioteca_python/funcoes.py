def adicionar_livro(ListaLivros):
    titulo = input("Adicione o título do livro: ")
    autor = input("Digite o autor do livro: ")
    livro = {
        "título": titulo,
        "autor": autor,
        "status": "disponível"
    }
    ListaLivros.append(livro)
    return ListaLivros

def emprestar_livro(ListaLivros):
    emprestar = input("Digite o título do livro que você quer emprestar: ")

    for i in ListaLivros:
       if i["titulo"] == emprestar: 
           if i["status"] == "disponível":
               i["status"] = "emprestado"
               return "Livro emprestdo com sucesso!"
           else:
               return "Esse livro já foi emprestado"
           
    return "Esse livro não é existente nessa biblioteca"

def devolver_livro(ListaLivros):
    devolver = input("Digite o título do livro que quer devolver: ")

    for i in ListaLivros:
        if i["titulo"] == devolver:
            if i["status"] == "emprestado":
                i["status"] = "disponível"
                return "Livro devolvido com sucesso!"
            else:
                return "Esse livro já foi devolvido e já se encontra disponível novamente"
            
    return "Histórico de livro não encontrado"

def exibir_livro(ListaLivros):
    for livros in ListaLivros:
        print("Título:", livros["titulo"])
        print("Status:", livros["status"])
        print()