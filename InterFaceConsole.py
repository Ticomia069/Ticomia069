#classe de serviço ao Usuario

class UserService: 
    def __init__(self, repository, user_repository: UserRepository):
        self._repository = repository

def __add_user(Self, name: str, age: int, email: str) -> user:
    user = user(name, age, email)
    Self._repository.__add_user(user)
    return user

class InterfaceConsole:
    def __init__(self, user_service: UserService):
        self._user_service = user_service


    def exibir_menu(self) -> None
        print("1. Adicionar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por nome")
        print("4. Sair")

    def Obter_entrada_usuario(self, prompt: str,validator: callable = None):
        while True: #loop infinito
            valor = input(prompt).strip()
            try:
                if validator:
                    validator(valor)
                    return valor
            except ValueError as e :
                print(f"erro: {e}")
                print("Por favor, tente novamente")
                return valor
