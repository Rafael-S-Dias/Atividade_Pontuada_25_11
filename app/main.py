import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    service.criar_usuario()
    service.deletar_usuario()
    service.atualizar_usuario()
    service.pesquisar_usuario()

    print("\nListando todos os usuarios: ")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

if __name__ == "__main__":
        main()