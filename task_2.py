# словари:
#
# 1. Дан список стран и городов каждой страны.
# Для каждого города укажите, в какой стране он находится.
#
# 2. Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями
# нашего словаря.

# # 1. (Как я поняла)
# cntr_city = ["Australia", "Brisbane",
#              "Japan", "Tokyo",
#              "France", "Paris",
#              "Germany", "Essen",
#              "China", "Beijing",
#              "Korea", "Seoul",
#              "Germany", "Stuttgart",
#              "Korea", "Pusan",
#              "Australia", "Melbourne",
#              "China", "Shanghai",
#              "Japan", "Nagoya",
#              "France", "Lyon"]
#
# cntr_cities = {}
# try:
#     for i in range(0, len(cntr_city), 2):   # Шаг 2, т.к. у нас страна указывается через 1 элемент
#         country = cntr_city[i] # Страна идет первой
#         city = cntr_city[i + 1] # А город вторым
#         if country not in cntr_cities: # Проверяем, если страна раньше не добавлена, то добавляем, но без дубликатов
#             cntr_cities[country] = []
#         cntr_cities[country].append(city) # Добавляем города к странам по ключу
#
#     for country, city in cntr_cities.items():
#         print(f"Country: {country}")
#         print(f"Cities: ")
#         for cit in city:
#             print(cit)
#         print()
#
# except ValueError as error:
#     print(error)
#
# except Exception as error:
#     print(error)


# 2.

# list_1 = ["Key_1", "Key_2", "Key_3", "Key_4", "Key_5"]
# list_2 = ["Item_1", "Item_2", "Item_3", "Item_4", "Item_5"]
#
# try:
#     list_3 = list(zip(list_1, list_2)) # Делаем из 2х списков 1 список из кортежей, в которых по 2 элемента
#     print(list_3)
#
#     new_dict = dict(list_3) # Делаем из списка словарь
#     print(new_dict)
#
# except ValueError as error:
#     print(error)
#
# except Exception as error:
#     print(error)