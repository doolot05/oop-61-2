class Phone:
    def __init__(self, model, name, color, cpu):
        self.model = model
        self.name = name
        self.color = color
        self.CPU = cpu
        self.battery = 100
    def call (self, number):
        if self.battery <= 0:
            print(f"{self.model} {self.name}: батарея разряжена, звонок невозможен.")
        else:
            self.battery -= 10
            print (f"{self.model} {self.name}: звонит на номер {number}. Заряд: {self.battery}%")
    def info(self):
        print(f"модель: {self.model}")
        print (f"название: {self.name}")
        print(f"цвет: {self.color}")
        print(f"CPU: {self.CPU}")
        print(f"заряд: {self.battery}%\n")
phone1 = Phone ("Samsung", "Galaxy 21 S","black","Snapdragon 888")
phone2 = Phone ("Iphone", "14 pro", "purple", "A17 Bionic")
phone3 = Phone ("Xiomi", "Mi 11", "white", "Snapdragon 870")
phone2.call ("0999-039-111")
phone3.call ("0999-039-112")
phone1.info()
