
import random

with open("games_list.txt") as my_file:
    print(random.choice(my_file.readlines()))