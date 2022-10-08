# Реализуйте алгоритм перемешивания списка.
import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print ("Исходный список: ", list)
mix_list = random.sample(list, len(list))
print ("Перемешанный список: ", mix_list)