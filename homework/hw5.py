class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
PERMISSIONS = {
    "admin": ["start", "ban", "stop"],
    "user": ["start", "message"]
}
def check_permission(command_name):
    def decorator(func):
        def wrapper(self, user: User):
            if command_name not in sum (PERMISSIONS.values(), []):
                print(f" Команда '{command_name}' не существует")
                return
            allowed_commands = PERMISSIONS.get(user.role, [])
            if command_name not in allowed_commands:
                print(f' Пользователь {user.username} не может выполнять команду "{command_name}"')
                return
            print(f'Пользователь {user.username} ({user.role}) выполняет команду {command_name}')
            func(self, user)
        return wrapper
    return decorator
class Comand_Handler:
    @check_permission("start")
    def start(self, user):
        print(" Система запущена")
    @check_permission("ban")
    def ban(self, user):
        print("Пользователь заблокирован")
    @check_permission("stop")
    def stop(self, user):
        print("Система остановлена")
    @check_permission("message")
    def message(self, user):
        print(f"Пользователь {user.username} отправил сообщение")

if __name__ == "__main__":
    admin = User("Доолот", "admin")
    user = User ("Долька", "user")
    handler = Comand_Handler()
    print("=== Команды администратора ===")
    handler.start(admin)
    handler.ban(admin)
    handler.stop(admin)

    print("\n=== Команды обычного пользователя ===")
    handler.start(user)
    handler.ban(user)
    handler.message(user)

