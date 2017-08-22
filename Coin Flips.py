import random

outcome = []
heads = 0
tails = 0

def flip():
    flip = random.randint(0,1)
    if flip == 0:
        return ('H')
    else:
        return ('T')

def main(num):
    for i in range(num):
        outcome.append(flip())
    
    print('Result is ' + ''.join(str(e) for e in outcome))
    print('Heads count: %i' %(outcome.count('H')))
    print('Tails count: %i' %(outcome.count('T')))
    

while True:
    userInput = int(input("How many coin flips?"))
    main(userInput)
    an = input('Do ou want to repeat? Y/N')
    if an.lower() == ('n'):
        break
    else:
        outcome[:] = []