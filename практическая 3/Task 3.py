num1 = input()
num2 = input()
try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except ValueError as e:
    print('Вы ввели не число')
