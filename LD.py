# Списки
my_list = [2, 3, 4, 5, 6, 7]
my_list.append('Python')
print(my_list)
my_list[0]
my_list[6]
my_list[1:4]
len(my_list)
my_list.index(6)
my_list.remove('Python')

# Словари

weather = {'city': 'Moscow', 'temperature': '20', 'wind': 'east'}
weather['city']
weather['temperature'] = 40
len(weather)
print(weather.get('country')) 
weather['date'] = '27.05.2017'
my_list = []
my_list.append({'temperature': 20, 'wind': 'east', 'city': 'Moscow', 'date': '25.05.2017'})
my_list.append({'temperature': 30, 'wind': 'east', 'city': 'Moscow', 'date': '26.05.2017'})
my_list.append({'temperature': 40, 'wind': 'east', 'city': 'Moscow', 'date': '27.05.2017'})
print(my_list)