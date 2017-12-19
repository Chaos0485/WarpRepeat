answers = {'Hi': 'Hello', 'How are you?': 'Better than you!', 'Bye' : 'Nice to meet you'}

question = input('Say something: ')	
answer = answers.get(question)
def get_answer(question):	
	return answer	
get_answer(Bye)