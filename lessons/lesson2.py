# Родительский\Супер класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} {self.lvl}"

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)

# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"{self.name} Салам!!"

    def cast_spell(self):
        return f"{self.name} кастует огненый шар!!!"

class WarriorHero(MageHero):
    def attack(self):
        return f"{self.name} наносит удар мечом!!!"

gandalf = MageHero("Gandalf", 100, 1000, 100)
aragon = WarriorHero("Aragon", 100, 1000, 99)

# print(kirito.action())
# print(gandalf.action())
# print(aragon.action())

# print(type(gandalf))
# print(type(kirito))




# class A:
#     def action(self):
#         print('A')
#
# class B(A):
#     def action(self):
#         super().action()
#         print('B')
#
# class C(A):
#     def action(self):
#         super().action()
#         print('C')
#
# class D(B,C):
#     def action(self):
#         super().action()
#         print('D')
#
#
# obj = D()
# obj.action()
# print(D.__mro__)






# class Animal:
#     def action(self):
#         return 'Animal'
#
# class Fly:
#     def action(self):
#         return 'Fly'
#
# class Swim:
#     def action(self):
#         return 'Swim'
#
#
#
# class Duck(Fly, Animal, Swim):
#     pass
#
# donald_duck = Duck()
# print(donald_duck.action())

# 2. Полиморфизм без наследования (duck typing)

class Car:
    def action(self):
        return "Машина едет"
class Numan:
    def action(self):
        return 'Человек идет'
class Snake:
    def action(self):
        return 'Змея ползет'

# 3. Полиморфизм через перегрузку операторов (ad-hoc polymorphism)
# print(5 + 5)
# print("5" + "5")
# print("5" + "5")
# print("5" + "5")
# print("5" + "5")
# print("5" + "5")
# print("5" + "5")
# print("5" + "5")
# print("5" + "5")