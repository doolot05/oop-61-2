class Animal:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health

    def info(self):
        return f"{self.name}, {self.age} лет, здоровье {self.health}"

    def use_ability(self):
        return f"{self.name} использует базовую способность."


# МИКСИНЫ
class Flyable:
    def use_ability(self):
        return super().use_ability() + " летает."


class Swimmable:
    def use_ability(self):
        return super().use_ability() + " плавает."


class Invisible:
    def use_ability(self):
        return super().use_ability() + " становится невидимым."


# ЖИВОТНЫЕ
class Duck(Flyable, Swimmable, Animal):
    pass


class Bat(Flyable, Invisible, Animal):
    pass


class Frog(Swimmable, Animal):
    pass


class Phoenix(Flyable, Invisible, Animal):
    def reborn(self):
        self.health = 200
        return f"{self.name} возродился из пепла!"


# ЗООПАРК
class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for a in self.animals:
            print(a.info())

    def perform_show(self):
        for a in self.animals:
            print(a.use_ability())
if __name__ == "__main__":
    zoo = Zoo()

    duck = Duck("Дональд", 3, 80)
    bat = Bat("Бэтти", 5, 60)
    frog = Frog("Кермит", 2, 50)
    phoenix = Phoenix("Феникс", 100, 200)

    # Добавляем животных в зоопарк
    for animal in (duck, bat, frog, phoenix):
        zoo.add_animal(animal)

    print("=== Информация о животных ===")
    zoo.show_all()

    print("\n=== Шоу суперспособностей ===")
    zoo.perform_show()

    print("\nMRO для Duck:", Duck.__mro__)
    print("MRO для Phoenix:", Phoenix.__mro__)
