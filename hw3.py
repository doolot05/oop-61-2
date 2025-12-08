# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.__discount = 0
#     def get_price(self):
#         """Возвращает цену со скидкой"""
#         final_price = self.price * (1- self.__discount/100)
#         return round(final_price, 2)
#     def set_discount(self, percent):
#         """Устанавливает если процент <=50"""
#         if 0 <= percent <= 50:
#             self.__discount = percent
#         else:
#             print("Ошибка, скидка не может быть больше 50%")
#     def apply_extra_discount(self, secret_code):
#         """Применяет вип скидку, если код правильный"""
#         if secret_code == "VIP312":
#             self.__discount += 5
# #Общая скидка не должна превышать 50+5=55
#         if self.__discount > 55:
#             self.__discount = 55
#         else:
#             print("Неверный код")
# p = Product("Iphone", 100000)
#
# p.set_discount(20)
# print("Цена со скидкой", p.get_price())
# p.apply_extra_discount("VIP312")
# print("Цена после Вип скидки", p.get_price())
# p.apply_extra_discount("Wrong")
# print("Итоговая цена", p.get_price())

#АБСТРАКЦИЯ
from abc import ABC, abstractmethod
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print({
            "type": "crypto",
            "amount": amount,
            "currency": "USDT"
        })

    def refund(self, amount):
        print({
            "type": "crypto_refund",
            "amount": amount,
            "currency": "USDT"
        })

class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)

processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)
