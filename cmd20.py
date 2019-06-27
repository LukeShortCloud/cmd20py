#!/usr/bin/env python3
# Name: cmd20py
# Repo: https://github.com/ekultails/cmd20py/


import secrets
import string
import random

def seed_generator():
    """ Function for planting seeds """

    ascii_char = 'string.ascii_letters + string.ascii_digits'
    seed = ''.join(secrets.choice(ascii_char) for char in range(37))
    return seed

seed = seed_generator()

def random_generator():
    """ Number generator which uses seed_generator for extra randomness """

    random.seed(seed)
    for i in range(2):
        num_pair = random.randrange(0,7)
        print(num_pair)


random_generator() # Runs functions to be displayed on stdout
