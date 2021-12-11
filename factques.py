import random
from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def createGold(self):
        pass

    @abstractmethod
    def createRed(self):
        pass

    @abstractmethod
    def createBrown(self):
        pass


class DragonFactory(AbstractFactory):

    def __init__(self, weigh, color, wing):
        self.weigh = weigh
        self.color = color
        self.wing = wing
        self.cost = 0
        self.animal = 'Dragon'
        self.special = 'Flying'

    def createGold(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

    def createRed(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

    def createBrown(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

class SalamanderFactory(AbstractFactory):

    def __init__(self, weigh, color, wing):
        self.weigh = weigh
        self.color = color
        self.wing = wing
        self.cost = 0
        self.animal = 'Salamander'
        self.special = 'Resistance'

    def createGold(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

    def createRed(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

    def createBrown(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

class DinosaurFactory(AbstractFactory):

    def __init__(self, weigh, color, wing):
        self.weigh = weigh
        self.color = color
        self.wing = wing
        self.cost = 0
        self.animal = 'Dinosaur'
        self.special = 'Fast_Running'

    def createGold(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

    def createRed(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))

    def createBrown(self):
        print('It\'s a {} {}, with {}meter wings, {}'.format(self.color, self.animal, self.wing, self.special))


class Client():
    def __init__(self):
        print('Welcome! What do you want to order?')

        while True:
            weigh = self.getWeigh()
            color = self.getColor()
            wing = self.getWing()
            print(weigh, color, wing)
            self.factory = self.getFactory(weigh, color, wing)
            self.factory.cost = self.getCost(weigh, color, wing)
            print(self.factory.cost)
            self.createColor(color)

            cont = int(input("Do you want to continue shopping? \n1.Yes \n2.No \nYour choice?:"))
            if cont == 2:
                print('Have a nice day!')
                break

    def getWing(self):
        wing = random.randint(0, 50)
        return wing

    def getWeigh(self):
        weigh = random.randint(100, 5000)
        return weigh

    def getColor(self):
        colors = ['Gold', 'Brown', 'Red']
        color = random.choice(colors)
        return color

    def getCost(self, weigh, color, wing):
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
        else:
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
        return cost


    def getFactory(self, weigh, color, wing):
        factory = None
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

    def createColor(self, color):
        if color == 'Gold':
            self.factory.createGold()
        elif color == 'Brown':
            self.factory.createBrown()
        else:
            self.factory.createRed()

if __name__ == "__main__":
    cl = Client()