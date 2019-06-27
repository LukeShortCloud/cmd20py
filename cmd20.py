#!/usr/bin/env python3
# Name: cmd20py
# Repo: https://github.com/ekultails/cmd20py/


import secrets
import string

def seed_generator():
    """ Function for planting seed """

    ascii_char = 'string.ascii_letters + string.ascii_digits'
    seed = ''.join(secrets.choice(ascii_char) for char in range(37))
