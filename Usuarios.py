import re
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str

    def __post_init__(self) -> None:
        self._validate_email()
        self._validate_age()

    def _validate_email(self) -> None:
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(padrao, self.email):
            raise ValueError(f"Email inválido: {self.email}")

    def _validate_age(self) -> None:
        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError(f"Idade inválida: {self.age}")

class UserRepository:
    def __init__(self):
        self._users: dict[str, User] = {}

    def add_user(self, user: User) -> None:
        if user.email in self._users:
            raise ValueError(f"Usuário com email {user.email} já existe")
        self._users[user.email] = user
        print(f"Usuário {user.name} adicionado com sucesso")

    def list_all(self) -> List[User]:
        return list(self._users.values())

    def search_user_by_name(self, name: str) -> List[User]:
        name = name.lower().strip()
        return [u for u in self._users.values() if name in u.name.lower()]

class UserService:
    def __init__(self):
        self._repository = UserRepository()

    def add_user(self, name: str, age: int, email: str) -> User:
        user = User(name=name, age=age, email=email)
        self._repository.add_user(user)
        return user

    def list_all(self) -> List[User]:
        return self._repository.list_all()

    def search_user_by_name(self, name: str) -> List[User]:
        return self._repository.search_user_by_name(name)

class InterfaceConsole:
    def __init__(self):
        self._user_service = UserService()

    def exibir_menu(self) -> None:
        print("\n=== Menu ===")
        print("1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário por nome")
        print("4. Sair")

    def obter_entrada_usuario(self, prompt: str, validator=None) -> str:
        while True:
            valor = input(prompt).strip()
            try:
                if validator:
                    return validator(valor)
                return valor
            except ValueError as e:
                print(f"Erro: {e}")
                print("Por favor, tente novamente")

    def adicionar_usuario(self) -> None:
        try:
            nome = self.obter_entrada_usuario("Nome: ")
            idade = int(self.obter_entrada_usuario("Idade: "))
            email = self.obter_entrada_usuario("Email: ")
            self._user_service.add_user(nome, idade, email)
            print("Usuário adicionado com sucesso!")
        except ValueError as e:
            print(f"Erro ao adicionar usuário: {e}")

    def executar(self) -> None:
        while True:
            self.exibir_menu()
            try:
                opcao = int(self.obter_entrada_usuario("Escolha uma opção: "))
                if opcao == 1:
                    self.adicionar_usuario()
                elif opcao == 2:
                    usuarios = self._user_service.list_all()
                    if not usuarios:
                        print("Nenhum usuário cadastrado")
                    for user in usuarios:
                        print(f"Nome: {user.name}, Idade: {user.age}, Email: {user.email}")
                elif opcao == 3:
                    nome = self.obter_entrada_usuario("Nome do usuário: ")
                    usuarios = self._user_service.search_user_by_name(nome)
                    if not usuarios:
                        print("Nenhum usuário encontrado")
                    for user in usuarios:
                        print(f"Nome: {user.name}, Idade: {user.age}, Email: {user.email}")
                elif opcao == 4:
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Digite um número.")

if __name__ == "__main__":
    interface = InterfaceConsole()
    interface.executar()
