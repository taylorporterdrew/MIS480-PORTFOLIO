# Taylor Porter
# MIS480 MOD6 OPTION_2
# Colorado State University - Global Campus


# This program will generate a random password

import random # This function is used to instruct the computer to pick a random number in a given range
import array as arr


# Used to set the maximum length necessary for the password
# The integer after "=" determines the specific length
MAX_LEN = 15

# Now we have to specify the characters that are needed in the password
# Another option here would be to use ASCII coded to represent the english characters
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                     'W', 'X', 'Y', 'Z']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '?', '>', '<']

# Now we will combine all the characters we listed above to form an array
# There are other ways to do this in python 
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# We will randomly select a character from each set of characters above
random_digit = random.choice(DIGITS)
random_upper = random.choice(UPCASE_CHARACTERS)
random_lower = random.choice(LOCASE_CHARACTERS)
random_symbol = random.choice(SYMBOLS)


# We uae a temporary variable to swap the values and combine the randomly selected characters above
# This means the password will only contain four characters since there were only four types specied
# We will change this later on since we want a 15 character password
# This also ensures that we have at least one of each character type
temp_pass = random_digit + random_upper + random_lower + random_symbol

# Now is later - so we will make sure to fill the rest of the characters of the password
# We do this by selecting randomly from the available characters from the combined list above
# We will use the range function to generate a list of values
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    # Now we will convert the password into an array
    # We will need to shuffle, using .shuffle, to ensure that their is no detectable pattern
    temp_pass_list = arr.array('c',temp_pass) #typecode
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x

print(password)

# References
# https://docs.python.org/3/library/array.html
