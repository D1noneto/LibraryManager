class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = {}

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def listarLivros(self):
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{livro.titulo} - {livro.autor} [{status}]")

    def emprestarLivro(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.emprestar()
                self.emprestimos[titulo] = usuario
                print(f"Livro '{titulo}' emprestado a {usuario.nome}.")
                return
        print("Livro não disponível.")

    def devolverLivro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.devolver()
                usuario = self.emprestimos.pop(titulo)
                print(f"Livro '{titulo}' devolvido por {usuario.nome}.")
                return
        print("Livro não está emprestado.")
