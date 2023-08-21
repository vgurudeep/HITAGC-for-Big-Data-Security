# A script to generate text file of given size

import string
import random

# size = int(input("Enter the size in MB"))
# size = 100
# new_size = size * 1024
all_char = list(string.printable)

file_title = f'{5}MB_Size.txt'
text_file = open(file_title, 'w+')

for i in range(5242880):
    text_file.write(random.choice(all_char))



