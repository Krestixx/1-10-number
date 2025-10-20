import random

secret = random.randint(1, 10)
attempts = 0
guessed = False

while not guessed:
    try:
        number = int(input('Компьютер выбрал число, введи своё: '))
        if number == secret:
            gambling = int(input('Вы угадали число!\n Продолжить - 1 \n Выйти - 2 \n Продолжить?: '))
            if gambling == 2:
                break
            if gambling == 1:
                secret = random.randint(1,10)
            
        else:
            if number > secret:
                print(f'Число заданное компьютером меньше чем: {number}')
            elif number < secret:
                print(f'Число заданное компьютером больше чем: {number}')

    except ValueError:
        print('Ввод принимает только числа')
    