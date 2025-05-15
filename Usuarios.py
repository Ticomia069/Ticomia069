from _typeshed import DataclassInstance
from collections import UserString
from dataclasses import dataclass
from re import split
from typing import List, Self



#classe que representa um usuario
@dataclass(frozen = True)   
class user:
 
    name: str
    age: int
    email:str

    def __post_init__(self) -> None:
    #validar os dados ao criar uma instancia
        Self._validateEmail()
        Self._validateAge()

    #metodo para validar o email
    def _validate_Email(self) -> None:

        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(padrao, self.email):
            raise ValueError(f"Email invalido: {self.email}")

    def _validate_Age(self) -> None:
        if not isinstance(self.age, int) or self.age < 0:

            raise ValueError(f"Idade invalida: {self.age}")

#classe do repositório de usuarios

class UserRepository:

    def __init__(self):
        self._users: dict[str, user] = {}

    def __add_user(self, user: user) -> None:
        if user.email in self._users:
            raise ValueError(f"Usuario com email {user.email} ja existe")
        #adiciona o usuario ao repositorio   
        self._users[user.email] = user
        print(f"Usuario {user.name} adicionado com sucesso")


    def __List_all(self) -> List[user]:
        print(f"Lista de usuarios: {self._users}")
        return list(self._users.values())
        #retorna a lista de usuarios do repositorio


    def search_user_by_email(self, email: str) -> user:

        name = name.lower().strip()
        return [u for u in Self._Users.values() if name in u.name.lower()]
    


    def search_user_by_name(self,name:str) ->list[user]:
        name = name.lower().strip()
        return [u for u in self.__users.values() if name in u.name.lower()] 


 #busca um usuario pelo email

class UserService: 
    def __init__(self, repository, user_repository: UserRepository):
        self._repository = repository

def __add_user(self, name: str, age: int, email: str) -> user:
    user = user(name, age, email)
    Self._repository.__add_user(user)
    return user

def list_users(self) -> List[user]:
        return self._repository.list_all()

def search_user_by_email(self, email: str) -> user | None:
        return self._repository.search_user_by_email(email)

def search_users_by_name(self, name: str) -> List[user]:
        return self._repository.search_users_by_name(name)


class InterfaceConsole:
    def __init__(self, user_service: UserService):

        print("1- adicionar usuario")
        print("2- Listar Usuarios")
        print("3- Excluir Usuarios")
        print("4- Buscar os UsuarioS")

