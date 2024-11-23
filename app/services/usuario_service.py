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

            self.repository.criar_usuario(usuario)
            print("Usuario criado com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def deletar_usuario(self):
        try:
            email = input("Digite o email do usuário que deseja deletar: ")

            cadastro = self.repository.pesquisar_usuario_por_email(email)
            if cadastro:
                self.repository.deletar_usuario(cadastro)
                print("Usuário deletado com sucesso")
                return
           
            print("Usuário não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_usuario(self):
        try:
            email = input("Digite o email do usuário que deseja atualizar: ")

            cadastro = self.repository.pesquisar_usuario_por_email(email)
            if cadastro:
                cadastro.nome = input("Digite o novo nome: ")
                cadastro.email = input("Digite o novo e-mail: ")
                cadastro.senha = input("Digite a nova senha: ")
                
                self.repository.atualizar_usuario(cadastro)
                print("Usuário atualizado com sucesso")
                return
            
            print("Usuário não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def pesquisar_usuario(self):
        try:
            email = input("Digite o email do usuário que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_usuario_por_email(email)
            if cadastro:
                print("Dados do usuário: ")
                print(f"\n Id: {cadastro.id} | Nome: {cadastro.nome} | Email: {cadastro.email}")
                return
            
            print("Usuário não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()