# Задание 1 и 2

names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
	print(name)

for name in names:
	print(name + ' ' + str(len(name)))


# Задание 3

is_male = {
  'Оля': False,
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
	print(name + ' ' + str(is_male[str(name)]))

# Задание 4

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print('Всего' + ' ' + str(len(groups)) + ' ' + 'группы.')
print('В' + ' ' + 'группе' + ' ' + str(len(groups[0])) + ' ' + 'ученика.') # и далее по номерам элементов

# или

for group in groups:
	print('В' + ' ' + 'группе' + ' ' + str(len(group)) + ' ' + 'ученика.')

# Задание 5

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

s = 0
for group in groups:
	s = s + groups.count(group)
	for student in group:
		print('Группа' + ' ' + str(s) + ':' + str(student))