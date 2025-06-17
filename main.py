class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def is_disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__emprestimos = {}

    def adicionarLivro(self, livro):
        self.__livros.append(livro)

    def listarLivros(self):
        for livro in self.__livros:
            status = "Disponível" if livro.is_disponivel() else "Emprestado"
            print(f"{livro.get_titulo()} - {livro.get_autor()} [{status}]")

    def emprestarLivro(self, titulo, usuario):
        for livro in self.__livros:
            if livro.get_titulo() == titulo and livro.is_disponivel():
                livro.emprestar()
                self.__emprestimos[titulo] = usuario
                print(f"Livro '{titulo}' emprestado a {usuario.get_nome()}.")
                return
        print("Livro não disponível.")

    def devolverLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo and not livro.is_disponivel():
                livro.devolver()
                usuario = self.__emprestimos.pop(titulo)
                print(f"Livro '{titulo}' devolvido por {usuario.get_nome()}.")
                return
        print("Livro não está emprestado.")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")
    usuario1 = Usuario("Maria", "maria@email.com")

    biblioteca.adicionarLivro(livro1)
    biblioteca.adicionarLivro(livro2)

    print("\nLista de livros disponíveis:")
    biblioteca.listarLivros()

    print("\nEmprestando livro '1984' para Maria:")
    biblioteca.emprestarLivro("1984", usuario1)

    print("\nLista de livros após o empréstimo:")
    biblioteca.listarLivros()

    print("\nDevolvendo o livro '1984':")
    biblioteca.devolverLivro("1984")

    print("\nLista de livros após a devolução:")
    biblioteca.listarLivros()