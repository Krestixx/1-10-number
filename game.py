import random

diff = int(input('Сложность\nЛегко - 1 \nСредне - 2 \nСложно - 3\nВаш выбор:'))

if diff == 1:
    secret = random.randint(1,10)
elif diff == 2:
     secret = random.randint(10,35)
else:
    secret = random.randint(25,75)


guessed = False
attempts = 0
while not guessed:
    try:
        number = int(input('Компьютер выбрал число, введи своё: '))
        attempts += 1
        if number == secret:
            gambling = int(input(f'Вы угадали число за {attempts} попыток!\n Продолжить - 1 \n Выйти - 2\n Сменить сложность - 3\n Продолжить?: '))     
            if gambling == 2:
                break            
            if gambling == 1:
                attempts = 0
                if diff == 1:
                    secret = random.randint(1,10)
                elif diff == 2:
                    secret = random.randint(10,35)
                else:
                    secret = random.randint(25,75)
            elif gambling == 3:
                attempts = 0
                diff = int(input('Сложность\nЛегко - 1 \nСредне - 2 \nСложно - 3\nВаш выбор:'))
                if diff == 1:
                    secret = random.randint(1,10)
                elif diff == 2:
                    secret = random.randint(10,35)
                else:
                    secret = random.randint(25,75)
         
        else:
            if number > secret:
                print(f'Число заданное компьютером меньше чем: {number}')
            elif number < secret:
                print(f'Число заданное компьютером больше чем: {number}')
    except ValueError:
        print('Ввод принимает только числа')
