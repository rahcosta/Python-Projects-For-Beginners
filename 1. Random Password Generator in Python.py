'''random.sample() Return a k length list of unique elements chosen from the population sequence or set.

str.join(iterable) Return a string which is the concatenation of the strings in iterable.
A TypeError will be raised if there are any non-string values in iterable, including bytes objects.'''

# Importing sample function:
from random import sample

# Importing string module:
import string

# Importing sleep function:
from time import sleep

print('-=' * 20)
print(f'Welcome to the Random Password Generator')
print('-=' * 20)

# The length of password:
length = int(input('Enter the length of password: '))

# Defining data:
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
punctuation = string.punctuation

# Combining data:
all = lower + upper + numbers + punctuation

# Password:
password = ''.join(sample(all, length))

print('Processing...')
sleep(2)
print(f'Your password is: \033[7m{password}\033[m')

# The code \033[7m...\033[m was used to colorized the password on terminal.