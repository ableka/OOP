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
                bl = Builder()
                bill = bl.check()
                first = input('This set of animals costs {}UAH. Will u buy this set?(Y/N): '.format(bill))
                if first == 'Y' or first == 'y':
                    # print('Please put in your name and your phone number: ')
                    # name = input('Name: ')
                    # phone = input('Phone: ')
                    # with open('orders.csv', 'a', encoding='UTF-8', newline='') as csvfile:
                    #     headers = ['Name', 'Phone', 'Animal', 'Cost']
                    #     date = datetime.date.today()
                    #     row = [name, phone, fb.factory.animal, fb.factory.cost, date]
                    #     writer = csv.writer(csvfile)
                    #
                    #     # writer.writerow(headers)
                    #     writer.writerow(row)
                    print('Thank you for buying a pet')
                else:
                    print('Sorry, but now you need to pay us tax for this pet')
                cont = int(input("Do you want to continue shopping? \n1.Yes \n2.No \nYour choice?:"))
                if cont == 2:
                    print('Have a nice day!')
                    break
        else:
            print('Okay, bye-bye((')


class Builder:

    def check(self):
        fb = Fabric()
        if fb.factory.animal == 'Kitty':
            full_cost = self.third(fb)
        elif fb.factory.animal == 'Salamander':
            full_cost = self.second(fb)
        else:
            full_cost = self.first(fb)
        return full_cost

    def to_file(self):
        pass

    @staticmethod
    def first(fb):
        full_cost = 0
        count_drg = 0
        count_din = 0
        while True:
            if fb.factory.animal == 'Dragon' and count_drg < 3:
                fb.factory.create_animal()
                full_cost = round(full_cost + fb.factory.cost, 2)
                count_drg += 1
            elif fb.factory.animal == 'Dinosaur' and count_din < 2:
                fb.factory.create_animal()
                full_cost = round(full_cost + fb.factory.cost, 2)
                count_din += 1
            else:
                full_cost = round(full_cost + fb.factory.cost / 3, 2)
            if count_drg == 3 and count_din == 2:
                break
            fb = Fabric()
        return full_cost

    @staticmethod
    def second(fb):
        full_cost = 0
        count_drg = 0
        count_slm = 0
        count_din = 0
        while True:
            if fb.factory.animal == 'Salamander' and count_slm < 1:
                fb.factory.create_animal()
                full_cost = round(full_cost + fb.factory.cost, 2)
                count_slm += 1
            elif fb.factory.animal == 'Dragon' and count_drg < 1:
                fb.factory.create_animal()
                full_cost = round(full_cost + fb.factory.cost, 2)
                count_drg += 1
            elif fb.factory.animal == 'Dinosaur' and count_din < 1:
                fb.factory.create_animal()
                full_cost = round(full_cost + fb.factory.cost, 2)
                count_din += 1
            else:
                full_cost = round(full_cost + fb.factory.cost / 3, 2)
            if count_drg == 1 and count_din == 1 and count_slm == 1:
                break
            fb = Fabric()
        return full_cost

    @staticmethod
    def third(fb):
        full_cost = 0
        count = 0
        while True:
            if fb.factory.animal == 'Kitty':
                fb.factory.create_animal()
                full_cost = round(full_cost + fb.factory.cost, 2)
                count += 1
            else:
                full_cost = round(full_cost + fb.factory.cost / 3, 2)
            if count == 3:
                break
            fb = Fabric()
        return full_cost


class Fabric:
    def __init__(self):
        weigh = self.get_weigh()
        color = self.get_color()
        wing = self.get_wing()
        self.factory = self.get_factory(weigh, color, wing)
        self.factory = self.adapt(weigh, color, wing)
        self.factory.cost = self.get_cost(weigh, color, wing)

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


if __name__ == "__main__":
    cl = Client()
