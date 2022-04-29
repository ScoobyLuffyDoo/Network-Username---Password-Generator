import random
from tokenize import Special
# import numpy as np

character_set ='abcdefghijklmnopqrstuvwxyz'
upper_character_set = character_set.upper()
numbers_set = "0123456789"
special_character='!@#$%^&*()_+=|?<>/'
all_characters = character_set+upper_character_set+numbers_set+special_character

class Generator():
    @staticmethod
    def get_password(length):
        # get new length
        tempset= random.choices(all_characters, k=length)
        password= "".join(tempset)
        return(password)
    

    def get_username():
        pass

