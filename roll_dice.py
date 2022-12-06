import random



y = True
n = False

while y == True:
    dice = random.randint(1,6)
    print(dice)
    
    if dice == 1:
        print('[   ]')
        print('[ 0 ]')
        print('[   ]')
    elif dice == 2:
        print('[0  ]')
        print('[   ]')
        print('[  0]')
    elif dice == 3:
        print('[0  ]')
        print('[ 0 ]')
        print('[  0]')
    elif dice == 4:
        print('[0 0]')
        print('[   ]')
        print('[0 0]')
    elif dice == 5:
        print('[0 0]')
        print('[ 0 ]')
        print('[0 0]')
    elif dice == 6:
        print('[0 0]')
        print('[0 0]')
        print('[0 0]')

    print('To Roll again type y below, to quit type n below')
    choice = input(' ')
    if choice == 'y' or choice == 'Y':
        y = True
    elif choice == 'n' or 'N':
        y = False

    dice = random.randint(1,6)