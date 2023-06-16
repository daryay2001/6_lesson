# 1. Дан список чисел. Уберите дубликаты значений. Вывести уникальные значения.
#
# 2. Даны два списка чисел.
#
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
#
# 3. Дан текст: в первой строке записано число строк, далее идут сами строки.
#
# Определите, сколько различных слов содержится в этом тексте.
#
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

# 1. Как вывести уникальные значения (т.е. те, которые не имеют повторов) Поправка

nums_1 = [1, 5, 8, 12, 14, 3, 8, 7, 9, 14]
nums_2 = []

for i in nums_1:
    if nums_1.count(i) == 1:
        nums_2.append(i)

print(nums_2)


#ver_1 Это как убрать дубликаты
# nums_1 = [1, 5, 8, 12, 14, 3, 8, 7, 9, 14]
# print(nums_1)
# nums_2 = set(nums_1)
# print(nums_2)
# print(type(nums_2))
# nums_2 = list(nums_2)
# print(nums_2)
#
# #ver_2 Как убрать дубликаты без использования set
#
# nums_3 = sorted(nums_1)
# print(nums_3)
# nums_4 = []
# for i in range(len(nums_3)):
#     if nums_3[i] != nums_3[i-1]:
#         nums_4.append(nums_3[i])
# print(nums_4)

#####

# 2. Я так понимаю, что нужно посчитать количество чисел, которые одновременно есть
# и в первом, и во втором списке

# list_1 = [1, 12, 36, 27, 81, 2, 36, 27]
# list_2 = [36, 85, 45, 1, 27, 2, 12, 8, 0, 9, 225]
#
# try:
#     lst_1 = set(list_1)
#     lst_2 = set(list_2)
#
#     lst_3 = lst_1.intersection(lst_2) # функция возвращает то, что есть и в 1м, и во 2м списке
#     print(lst_3)
#
#     total_num = 0
#
#     for i in lst_3:
#         total_num += 1
#     print(f"Total amount of numbers which are in both lists: {total_num}")
#
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)
# 3.

# text = "в первой строке записано число строк, далее идут сами строки."
# print(text)
# try:
#     SEPARATOR = " " # в данном случае сепаратором явл пробел, т.к. предложение одно и слова раздел пробелом.
#     sep_words = text.split(SEPARATOR)
#     print(sep_words)
#
#     sep_2 = sorted(sep_words) # сортируем слова для последовательного сравнения
#     print(sep_2)
#
#     count = 0
#     for i in range(0, len(sep_2)):
#         if sep_2[i] != sep_2[i - 1]:
#             count += 1
#     print(f"There are {count} different words in this sentence.")
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)

