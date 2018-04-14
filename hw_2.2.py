# print('Решение домашнего задания по лекции 2.2 "Работа с кодировками, русскими буквами"')

some_text = 'Hello, мир!'
print(some_text.encode('koi8-r'))
print('list koi8-r', list(some_text.encode('koi8-r')))
print('list cp1251', list(some_text.encode('cp1251')))
print('list utf8', list(some_text.encode('utf8')))

data = bytes([72, 101, 108, 108, 111, 44, 32, 236, 232, 240, 33])
print('decode cp1251', data.decode('cp1251'))

# закончил просмотр вебинара на 24 минуте