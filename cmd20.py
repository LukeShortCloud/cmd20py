#!/usr/bin/env python3
# Name: cmd20py
# Repo: https://github.com/ekultails/cmd20py/

import random

# Number Generator
random.seed(None)
die1 = random.randrange(0,7)
die2 = random.randrange(0,7)
die_results_msg = "You rolled a:"
print(die_results_msg,die1,die2)
