'''hi_there'''
import random



def choose():
    '''fuck you'''
    with open("games_list.txt", "r", encoding= "utf-8") as my_file:
        choice = random.choice(my_file.readlines())
        #print(choice)
        return choice


if __name__ == "__main__":
    print(choose())




    # '''
    # with open("games_list.txt") as my_file:
    #     choice = random.choice(my_file.readlines())
    # '''