import random


inputpassword = input("Define a 6 digit password constructed of a, b, c, d, e , f ]")

AvailableChrs = ['a', 'b', 'c', 'd', 'e', 'f']

result = ''
username = ''
Password = inputpassword

count = 0
while result != Password:
    result = AvailableChrs[random.randrange(0, 6)] + AvailableChrs[random.randrange(0, 6)] + AvailableChrs[random.randrange(0, 6)] + AvailableChrs[random.randrange(0, 6)] + AvailableChrs[random.randrange(0, 6)] +  AvailableChrs[random.randrange(0, 6)]

    count = count + 1
    print('Bruteforce attack with = ', result, ' and the count is', count)
