school_scores = [{'school_class': '1a', 'scores': [3,3,5,4,2]},
				{'school_class': '2b', 'scores': [2,5,5,3,4]},
				{'school_class': '3c', 'scores': [5,3,4,5,1]}]

for classes in [0, 1, 2]: # classes - номер элемента
	print(classes)

x = sum(school_scores[classes]['scores'])/len(school_scores[classes]['scores']) # считаем среднее значение по всей школе, сумма элементов значения списка по ключу 'scores' ищ словаря classes делим на длину этого самого списка для всех classes
print(x) # [3.6] по всей школе, для вычисления по каждому классу отдельно подставляем вместо классес непосредственно сам номер словаря в списке.
