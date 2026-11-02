my_list = [1, 2, 3]
print(my_list)
my_list[0] = 100
print(my_list) #элемент изменился тк список изменяемый тип данных

my_tuple = (1, 2, 3)
print(my_tuple)
try:
    my_tuple[0] = 100
except TypeError as e:
    print(e)
print(my_tuple) #элемент не изменился тк кортеж неизменяемый тип данных

my_string = 'cat'
print(my_string)
try:
    my_string[0] = 'b'
except TypeError as z:
    print(z)
print(my_string) #элемент не изменился тк строка неизменяемый тип данных