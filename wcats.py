import random
import csv
import datetime


class DragonFactory:

    def __init__(self, weigh, color, wing):
        self.weigh = weigh
        self.color = color
        self.wing = wing
        self.cost = 0
        self.animal = 'Dragon'
        self.special = 'Flying'

    def create_animal(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))


class SalamanderFactory:

    def __init__(self, weigh, color, wing):
        self.weigh = weigh
        self.color = color
        self.wing = wing
        self.cost = 0
        self.animal = 'Salamander'
        self.special = 'Resistance'

    def create_animal(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))


class DinosaurFactory:

    def __init__(self, weigh, color, wing):
        self.weigh = weigh
        self.color = color
        self.wing = wing
        self.cost = 0
        self.animal = 'Dinosaur'
        self.special = 'Fast_Running'

    def create_animal(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))


class KittyFactory:

    def __init__(self):
        self.weigh = random.randint(5, 12)
        self.color = random.choice(['Red', 'Yellow'])
        self.wing = random.randint(0, 5)
        self.cost = 5000
        self.animal = 'Kitty'
        self.special = 'Kawaii'

    def create_animal(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))


class Client:
    def __init__(self):
        start = input('Welcome! Do you want to order a pet?:)')
        if start == '':
            while True:
                fb = Fabric()
                tax = round(fb.factory.cost / 3, 2)
                first = input('This pet costs {}UAH. Will u buy this pet?(Y/N): '.format(fb.factory.cost))
                if first == 'Y' or first == 'y':
                    print('Please put in your name and your phone number: ')
                    name = input('Name: ')
                    phone = input('Phone: ')
                    with open('orders.csv', 'a', encoding='UTF-8', newline='') as csv_file:
                        date = datetime.date.today()
                        row = [name, phone, fb.factory.animal, fb.factory.cost, date]
                        writer = csv.writer(csv_file)
                        writer.writerow(row)
                    print('Thank you for buying a pet')
                else:
                    print('Sorry, but now you need to pay us {}UAH tax for this pet'. format(tax))
                cont = int(input("Do you want to continue shopping? \n1.Yes \n2.No \nYour choice?:"))
                if cont == 2:
                    print('Have a nice day!')
                    break
        else:
            print('Okay, bye-bye((')


class Fabric:
    def __init__(self):
        weigh = self.get_weigh()
        color = self.get_color()
        wing = self.get_wing()
        self.factory = self.get_factory(weigh, color, wing)
        self.factory = self.adapt(weigh, color, wing)
        self.factory.cost = self.get_cost(weigh, color, wing)
        self.create_animals()

    @staticmethod
    def get_wing():
        wing = random.randint(0, 50)
        return wing

    @staticmethod
    def get_weigh():
        weigh = random.randint(100, 5000)
        return weigh

    @staticmethod
    def get_color():
        colors = ['Gold', 'Brown', 'Red']
        color = random.choice(colors)
        return color

    def get_cost(self, weigh, color, wing):
        if self.factory.animal == 'Dragon':
            if 100 < weigh < 300 and 30 < wing < 50:
                delta_w = (abs((weigh / 150) - 1))
                delta_wing = (abs((wing / 50) - 1))
                if color != 'Gold':
                    delta_c = 1
                else:
                    delta_c = 0
                cost = round((((1 - delta_w) + (1 - delta_c) + (1 - delta_wing)) / 3) * 3000000, 2)
            else:
                cost = 3000000
        elif self.factory.animal == 'Salamander':
            if 300 < weigh < 1500 and 10 < wing < 30:
                delta_w = (abs((weigh / 900) - 1))
                delta_wing = (abs((wing / 15) - 1))
                if color != 'Red':
                    delta_c = 1
                else:
                    delta_c = 0
                cost = round((((1 - delta_w) + (1 - delta_c) + (1 - delta_wing)) / 3) * 1000000, 2)
            else:
                cost = 1000000
        elif self.factory.animal == 'Dinosaur':
            if 1500 < weigh < 5000 and 0 < wing < 5:
                delta_w = (abs((weigh / 3250) - 1))
                delta_wing = (abs((wing / 5) - 1))
                if color != 'Brown':
                    delta_c = 1
                else:
                    delta_c = 0
                cost = round((((1 - delta_w) + (1 - delta_c) + (1 - delta_wing)) / 3) * 2200000, 2)
            else:
                cost = 2200000
        else:
            cost = 5000
        return cost

    def adapt(self, weigh, color, wing):
        if 200 < weigh < 600 or 20 < wing < 40:
            factory = KittyFactory()
        else:
            factory = self.get_factory(weigh, color, wing)
        return factory

    @staticmethod
    def get_factory(weigh, color, wing):
        if weigh < 300:
            if color == 'Red':
                factory = SalamanderFactory(weigh, color, wing)
            elif wing < 5:
                factory = SalamanderFactory(weigh, color, wing)
            else:
                factory = DragonFactory(weigh, color, wing)
        elif color == 'Red':
            factory = SalamanderFactory(weigh, color, wing)
        elif wing < 5:
            if weigh < 300:
                factory = SalamanderFactory(weigh, color, wing)
            elif color == 'Red':
                factory = SalamanderFactory(weigh, color, wing)
            else:
                factory = DinosaurFactory(weigh, color, wing)
        else:
            factory = SalamanderFactory(weigh, color, wing)
        return factory

    def create_animals(self):
        self.factory.create_animal()


if __name__ == "__main__":
    cl = Client()
