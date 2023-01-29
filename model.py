
names = ['Крылов К.С.', 'Носов А.Н.', 'Иванов А.А.']
tel = ['88885553344\n', '88885553345\n', '88885553346\n']


def printTelef():
     list = []
     for i in range(len(names)):
         list.append(names[i])
         list.append(tel[i])
     print(' '.join(list))


def addTelef():
     name = input("Введите Ф.И.О.: ")
     telephone = input("Введите телефон: ") + '\n'

     names.append(name)
     tel.append(telephone)
     print('Данные добавлены')

def serchTelef():
     name = input("Введите Ф.И.О.: ")
     for i in range(len(names)):
         if name in names[i] : print(names[i] + ' ' + tel[i])


def saveAsHTML():

     book = open('book.html', 'w', encoding='utf-8')
     for i in range(len(names)):
         book.write(names[i])
         book.write(' ')
         book.write(tel[i])
         book.write('<br>')

     print('Файл "book.html" сохранен')


def saveAsXML():

     book = open('book.xml', 'w', encoding='utf-8')
     for i in range(len(names)):
         book.write(names[i])
         book.write(' ')
         book.write(tel[i])

     print('Файл "book.xml" сохранен')