import random

print('Welcome to Coin Toss Game !')
choice = input('Please make your call "heads" or "tails" : ').lower()
result = random.randint(0, 1)
if result == 0:
    print("Its heads. You Won !")
else:
    print("Its tails. You Won !")
