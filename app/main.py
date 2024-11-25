import os
import time
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def menu():
        while True:
            print("======== SENAI SOLUTION =========")
            print("BEM VINDO!\n")
            print("1 - Adicionar usuário \n2 - Pesquisar um usuário \n3 - Atualizar dados de um usuário \
                \n4 - Excluir um usuário \n5 - Exibir todos os usuários cadastrados \n0 - Sair")
            
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                print("Comando inválido! Por favor, insira um número inteiro.")
                return 

            match opcao:
                case 1:
                    os.system("cls || clear")
                    service.criar_usuario()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    service.pesquisar_usuario()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    service.atualizar_usuario()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    service.deletar_usuario()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    print("\nListando todos os usuários: ")
                    usuarios = service.listar_todos_usuarios()

                    for usuario in usuarios:
                        print(f"{usuario.id} - {usuario.nome} - {usuario.email}") 
                        time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)


    menu()

if __name__ == "__main__":
        main()