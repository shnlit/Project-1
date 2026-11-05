name = str(input('Введите ваше имя: '))
age = int(input('Введите ваш возраст: '))
subjects = input('Введите ваши любимые предметы: ')

student = {
    'name': name,
    'age': age,
    'subjects': subjects
}

print('-' * 20)
print('АНКЕТА СТУДЕНТА')
print('-' * 20)

print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")
