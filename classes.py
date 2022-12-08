from utility import *
# import color
import colorama
from colorama import Fore
colorama.init(autoreset=True)

class Opportunity(Winningnumber3):
    def luckeey(self, powerball_numbers):
        print(f'Today’s Powerball winning numbers of The result.:, ' + Fore.LIGHTMAGENTA_EX + f"{self.user_numbers}",
              Fore.YELLOW + f'{self.user_Lottery}')
        print(Fore.RESET + f'The result based on your lucky numbers:' + Fore.LIGHTMAGENTA_EX +f"{self.winning_num}",
              Fore.YELLOW  + f' {self.powerball_loteery}')
        print(Fore.RESET + f'I got this one {self.powerball_numbers} correct numbers')
        if self.user_Lottery == self.powerball_loteery and powerball_numbers == 0:
            print("I got this one  4$")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 1:
            print("I got this one  4$")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 2:
            print("I got this one  7$ ")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 3:
            print("I got this one  7$ ")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 3:
            print("I got this one  100$")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 4:
            print("I got this one  100$ ")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 4:
            print("I got this one  10000$")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 5:
            print("I got this one  1000000$")
        elif self.user_Lottery == self.powerball_loteery and powerball_numbers == 5:
            print("I got this one  $324000000")
        else:
            print("try again")
        # boll = input("Are yuo want to continue? y/n :")
