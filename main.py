from client import Client
from formulas import *


def main():

    print("Welcome to the calculator bmi and bmr, put your datas to calculate!\n ")

    name = input('Your name: ')
    age_str = input('Your age: ')
    age = float(age_str)
    height_str = input('Your height: ')
    height = float(height_str)
    weight_str = input('Your weight: ')
    weight = float(weight_str)
    sex = input('Your Sex using "M" or "F": ')

    client = Client(name, age, height, weight, sex)
    bmi = calculate_bmi(client)
    bmr = calculate_bmr(client)

    print(f'Your Bmi is: {bmi: .2f}')
    print(f'Your Bmr is: {bmr: .2f}')


if __name__ == "__main__":
    main()
