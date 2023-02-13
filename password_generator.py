"""Create a random password generator using loops"""

import random

word = "hello"

for i in range(0,5):
    random_word = random.choice(word)
print(random_word)