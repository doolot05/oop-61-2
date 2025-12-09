# # class Hero:
# #     def __init__(self, name, age, hp):
# #         self.name = name
# #         self.age = age
# #         self.hp = hp
# #     def action (self):
# #         print(f"{self.name} к бою готов!")
# # class MageHero(Hero):
# #     def __init__(self, name, age, hp, mp):
# #         super ().__init__(name, age, hp)
# #         self.mp = mp
# #     def action (self):
# #         print(f"Маг{self.name} кастует заклинание! MP: {self.mp}")
# #
# # class WarriorHero(MageHero):
# #     def __init__(self, name, lvl, hp, mp, rage):
# #         super().__init__(name, lvl, hp, mp)
# #         self.rage = rage
# #     def action (self):
# #         print (f"Воин {self.name} атакует мечом! Ярость: {self.rage}")
# # h1= Hero ("Артур", 1, 1000)
# # m1= MageHero ("Гендальф", 5, 80, 120)
# # w1= WarriorHero ("Лагерта", 7, 150, 50, 30)
# #
# # h1.action()
# # m1.action()
# # w1.action()
# #
# #
#
# class Hero:
#     def __init__(self, name, lvl, hero_class):
#         self.name = name
#         self.lvl = lvl
#         self.hero_class = hero_class
#     def __eq__(self, other):
#         if not isinstance(other, Hero):
#             return False
#         return self.name == other.name and self.lvl == other.lvl
#     def __str__(self):
#         return f"{self.hero_class}: {self.name} (lvl {self.lvl})"
#
# class BankAccount:
#     def __init__(self, hero, bank_name, balance, password):
#         self.hero = hero
#         self.bank_name = bank_name
#         self._balance = balance
#         self.__password = password
#     def login(self, password):
#         return password == self.__password
#     @property
#     def full_info(self):
#         return f"Герой:{self.hero}, баланс: {self._balance} Som"
#
#     def get_bank_name(self):
#         return self.bank_name
#     def bonus_for_level(self):
#         return self.hero.level * 10
#
#     def __str__(self):
#         return f"{self.hero} Баланс: {self._balance} Som"
#     def __add__(self, other):
#         if not isinstance(other, BankAccount):
#            raise TypeError ("Можно складывать только счета")
#         if self.hero.hero_class != other.hero.hero_class:
#             raise TypeError ("Герои разных классов! Складывать нельзя")
#         return self._balance + other._balance
#     def __eq__(self, other):
#         """Герои равны, если равны их имена и уровни"""
#         return self.hero == other.hero
#
# h1 = Hero ("Doolot", 5, "Mage")
# h2 = Hero ("Doolot", 6, "Mage")
# h3 = Hero ("Daulet", 7, "Mage")
#
# acc1 = BankAccount (h1, "Optima Bank", 300, 123)
# acc2 = BankAccount (h2, "Optima Bank", 200, 1232)
# acc3 = BankAccount (h3, "Bakai Bank", 150, 1233)
# print(acc1.full_info)
# print (acc1+acc2)
# print (acc1==acc2)
# print (acc1==acc3)
# print (acc1)

#Абстрактный класс
from abc import ABC, abstractmethod
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass
class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"
class RuSms(SmsService):
    def send_otp(self, phone):
        return {
            "text": "Код: 1234",
            "phone": phone
        }
sms=KGSms()
print(sms.send_otp("999039111"))
sms_ru=RuSms()
print(sms_ru.send_otp("+7149325927580"))