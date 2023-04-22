### function to generate hashes that can be used as passwords

import random 

def pw_gen(length): 
    """function to generate the hash"""
    lower_case = 'abcdefghijklmnopqrutuvz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVZ'
    numbers= '0123456789'
    symbols= '!@#$%^&*'
    all = lower_case + upper_case + numbers + symbols
    password = "".join(random.sample(all,length))
    return password

##print your new hash, adjust the length to your desire
print(str(pw_gen(40)))