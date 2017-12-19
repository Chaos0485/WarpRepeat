Mylist = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

while True:
	name = Mylist.pop()
	if name == "Валера":
		print("Валера нашелся!")
		break

def find_person(name):
	while True:
		if name in Mylist:
			print('{} в списке'.format(name))
			break
		else:
			print("Такого нет.")
			break
find_person("Петя")

def ask_user(say):
	while True:
		say = input('Say something: ')
		if say == 'something':
			print('Well done!')
			break
		else:
			print('Man, come on...')	

answers = {'Hi': 'Hello', 'How are you?': 'Better than you!', 'Bye' : 'Nice to meet you'}

def get_answer(question, answer):	
question = input('Say something: ')	
answer = answers.get('{}.format.question')
	return answer	