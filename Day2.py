import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    a=tip_percent/100*meal_cost
    b=tax_percent/100*meal_cost
    print(round(a+b+meal_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
