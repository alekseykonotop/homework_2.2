# print('Решение домашнего задания по лекции 2.2 "Работа с кодировками, русскими буквами"')
# Задача: по каждому файлу новостей вывести список 10 самых частовстречающихся слов
# длинной более 6 символов.
# == Алгоритм решения ==
#    Программа должна
# 0. Спрашивать у пользователя какой файл стоит проверить.
# 1. Открыть и декодировать текстовый файл
# 2. Создать множество из слов в этом файле, которые длиннее 6 символов
# 3. Для каждого элемента множества подсчитать сколько раз этот эл. встречается
#    в декодированном тексте и записать значение в словарь где ключ - слово, значение - кол-во слова в тексте
# 4. Создать массив состоящий из словарей, в котором только 1 пара (слово : кол-во вхождения)
# 5. Отсортировать массив по значению в словаре, т.е. по кол-ву вхождения ( слева самые частовстречаемые слова)
# 6. Вывести на экран только первые 10 элементов массива




from chardet.universaldetector import UniversalDetector

# import chardet
#
#
# with open('newscy.txt', 'rb') as f:
#     data = f.read()
#     # print(data[:50])
#     result = chardet.detect(data)
#     print(result)
#     s = data.decode(result['encoding'])
#     print('s', s[:350])

# detector = UniversalDetector()
#
# with open('newscy.txt', 'rb') as f:
#     for line in f:
#         detector.feed(line)
#         if detector.done:
#             print(detector.result)
#             break
# detector.close()
# print(detector.result)


