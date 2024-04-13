#fill an array with 10 rando integers. Then search the array to discover whether or not it contains an integer input from the keyboard

import random

arr = []
for x in range(10):
    arr.append(random.randint(0,20))

answer = False
while not answer:
      num = int(input('Guess a number between 0-20: '))
      if num in arr:
           print('Given number exits in the array!')
           print(arr)
           answer = True
      else:
            print('Given number does not exits in the array!')
