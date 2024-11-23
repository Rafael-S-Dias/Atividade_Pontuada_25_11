from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self) :
        try:
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")
            senha = input("Digite seu senha: ")
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastro = self.repository.pesquisar_usuario_por_email(email=usuario.email)
            if cadastro:
                print("Usuário já cadastrado")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    # def deletar_aluno(self):
    #     try:
            
    #         aluno = 
    #         self.repository.deletar_aluno(aluno)
    #         print("Aluno deletado com sucesso")
    #     except TypeError as e:
    #         print(f"Erro ao deletar o arquivo: {e}")
    #     except Exception as e:
    #         print(f"Ocorreu um erro inesperado: {e}")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()