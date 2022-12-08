import random
from random import randint

class Winningnumber2():

    def __init__(self):
        self.winning_num = []
        self.powerball_loteery = []


    def ball(self):
        for num in range(0, 5):
            user_number = randint(1, 20)
            self.winning_num.append(user_number)
        lucky = random.randint(1,10)
        self.powerball_loteery.append(lucky)

class Winningnumber1(Winningnumber2):
    def __init__(self):
        super().__init__()
        self.user_numbers = []
        self.user_Lottery = []

    def use(self):
        for num in range(0, 5):
            user_numbers = randint(1, 20)
            self.user_numbers.append(user_numbers)
        whball = randint(1, 10)
        self.user_Lottery.append(whball)


class Winningnumber3(Winningnumber1):

    def game(self):
        self.powerball_numbers = len(set(self.winning_num).intersection(set(self.user_numbers)))
        return self.powerball_numbers
