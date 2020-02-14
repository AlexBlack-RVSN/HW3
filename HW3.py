#Задание 1.
def div_func():
    try:
        var_1 = int(input('Введите первое число: '))
        var_2 = int(input("Введите второе число: "))
        div = var_1 / var_2
    except ZeroDivisionError:
        return "На 0 деление запрещенно!!!"
    return div
print(div_func())

#Задание 2.
def info(**kwargs):
    name = str(input('Введите ваше имя: '))
    surname = str(input('Введите вашу фамилию: '))
    age = int(input('Введите ваш год рождения: '))
    city = str(input('Введите ваш город: '))
    email = str(input('Введите ваш email: '))
    tel = int(input('Введите ваш телефон: '))
    data = (f'{name} {surname} {age} {city} {email} {tel}')
    return data
print(info())

#Задание 3.
def my_func():
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    num3 = int(input('Введите третье число: '))
    s = [num1, num2, num3]
    s.remove(min(num1,num2,num3))
    return sum(s)
print(my_func())

#Задание 4.
def my_func():
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число со знакомом "-": '))
    z = x**y
    return z
print(my_func())

def my_func(x,y):
    return pow(x,y)
print(my_func(2,-2))

#задание 5.
def sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или Q, чтобы выйти: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма: {sum_res}')
sum()


#Задание 6.
def int_func(*args):
    text = input('Введите предлжение: ')
    print(text.title())

int_func()
