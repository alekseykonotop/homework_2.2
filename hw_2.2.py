import chardet

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

# with open('newscy.txt', 'rb') as f:
#     data = f.read()
#     # print(data[:50])
#     result = chardet.detect(data)
#     print(result)
#     s = data.decode(result['encoding'])
#     print('s', s[:350])

# Функ. открытия и декодирования файла + формирует список слов длинной больше 6 символов
# Функ. создает множество значений слов из текста и подсчитывает сколько каждое слово из
#       множества встречается в текстовом файле
# Функ. сортировки по убыванию, возвращает первые 10 значений
# Функ. вывода на экран самых частовстречаемых в тексте первых 10 слов в файлах +
# Функ. запуска приложения +


def open_and_read_file(article):
    '''Функция открывает переданный файл,

    декодирует его с помощью импортируемой фунции chardet,
    создает список из всех слов, длинной больше 6 символов, в файле.
    '''
    result_list = []
    with open(article, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        s_list = s.strip().split(' ')
        for word in s_list:
            if len(word) > 6:
                result_list.append(word)
    return result_list


def count_words_in_list(article):
    '''Функция получает на вход атрибут с названием файла,

    для передачи этого значения функции open_and_read_file(article).
    Получая от нее список используемых в файле слов, формирует множество,
    с помощью которого получает значения кол-ва вхождения каждого элемента
    множества в полученном списке.
    '''
    count_words_list = []
    words_lst = open_and_read_file(article)
    set_of_words = set(words_lst)
    for word_of_set in set_of_words:
        quantity = 0
        for i in words_lst:
            if i == word_of_set:
                quantity += 1
        count_words_list = count_words_list + [[word_of_set, quantity]]
    return count_words_list


def get_top_words_list(article):
    ''' Функция сортирует элементы списка по второму значению.

    Элементы списка являются спискамии. Функция возвращает
    список  из 10 отсортированных слов с максимальной частотностью в
    порядке убывания.
    '''
    lst = count_words_in_list(article)
    while True:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i][1] < lst[i+1][1]:
                lst[i][1], lst[i+1][1] = lst[i+1][1], lst[i][1]
                sorted = False
        if sorted:
            break
    return lst[:10]


def print_result(article, top_words_list):
    '''Функция print_result выводит на экран название

    файла и полученный список максимальных значений.
    '''
    print('В файле {0} самые высокочастотные слова: {1}\n'.format(article, top_words_list))



def ten_most_used_words():
    '''Функция определяет 10 самых высокочастотных слов с заданных файлах'''
    article_list = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']
    for article in article_list:
        top_words_list = get_top_words_list(article)
        print_result(article, top_words_list)


ten_most_used_words()
