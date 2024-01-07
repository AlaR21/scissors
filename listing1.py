# x = 13 % 5
# print(x)
# spam = "spam " * 10
# print(spam)
#
# lista = [1, 2, 3, 4]
# print(1 in lista)
# print(5 not in lista)


# # := nowosc w pythonie, operator przypisania
# if (n := len(lista)) >10:
#     print('boom')
# # else: print('nope')
# #
# imie = "Kunegunda"
# print(imie[::2])
# print(imie[-2])
# print(imie[:-4:-1])
#
# nazwisko = 'borasinska'
# print(nazwisko[:-4:-1])
#
# nazwa = 'abrakadabra'
# print(nazwa[:-4:-1])
#
# # skosk minusowy - > liczenie od tyłu
#
# # print(imie.count('n'))
#
# print('Małgorzata'.count('a'))
#
# print(imie.lower())
#
# print('NATALIA'.lower())
# print('łukaszek'.upper())
#
# print(len('natalia'))
# print(len('abrakadabra'))


# sentence = input('Wpisz dowolne zdanie: \n')
# sentence = sentence.strip()
# print(sentence.strip())

# lstrip()
# rstrip()
# #
# words = "Ania jest super"
# print(words.split(' '))
# print('W podanym zdaniu jest ', len(words), ' znakow')
#
# print('Czy zdanie rozpoczyna się wielką literą? ->', words[0].istitle())
# print('Czy zdanie rozpoczyna się literą? ->', words[0].isalpha())

# num = input('Wpisz dowolna liczbe: \n')
# print('Czy liczba jest liczbą całkowitą? ->', num.isdigit())
#
# interest = 'I love climbing'
# interest2 = interest.replace('climbing', 'hiking')
# print(interest2)

# fruit = 'apple, strawberry, cherry, apple, banana, orange'
# fruit2 = fruit.replace('apple', 'mango', 1)
# print(fruit2)


# string.replace(oldvalue, newvalue, count) jesli count niezdefiniowane - zmien

# num = '10'
# num2 = num.zfill(5)
# print(num2)

# dodaje zera na poczatku do stringa


# Formatowanie łańcucha znaków

# zdanie = input('Podaj dowolny tekst: \n')
# imie = 'Natalia'
# nazwisko = 'Łach'
# litera1 = nazwisko[3]
# litera2 = imie[2]
# liczba_liter1 = zdanie.count('h')
# liczba_liter2 = zdanie.count('t')
# # print(f'W podanym tekscie jest {liczba_liter1} liter {litera1} oraz {liczba_liter2} liter {litera2}.')
# #
#
# print(f'Wynik dodawania 33.33 oraz 66.67 to {33.33 + 66.66:.4f}')
# imie = 'natalia'
# print(f'Imie zapisane wielkimi literami to {imie.capitalize()}')
#
#
# godnosc = 'Katarzyna'
# print(godnosc[2])


# Typ list
#
# lista = [1,2,3]
# print(lista[2])

# lista = []
# lista_1 = [1, 11, 111, 1111]
# lista_2 = [2, 22, 222, 2222]
# lista_1.append([3, 33, 333])
# print(lista_1)
# #
# lista_1[2] = 4444
# print(lista_1)
#
# lista = []
# lista.append([1, 11, 111])
# lista.append([2, 22, 222])
# print(lista)
#
#
# print(lista[1][2])


# lista_7 = [2, 4, 8, 16, 5, 3, 1]
# posortowana = sorted(lista_7)
# # print(posortowana)
#
# lista3 = [1, 2, 3]
# lista4 = ['a', 5, 'Python', 7.8]
#
# lista3.extend(lista4)
# print(lista3)
#
# skala = [1, 2, 3, 4, 5, 6]
# skala.append(7)
# skala[7:] = [8]
# skala[len(skala):] = [9]
# print(skala)
#
#
# skala.insert(7, 11)
# print(skala)
#
# skala.pop()
# print(skala)
#
# skala.pop(2)
# print(skala)

# order = [1, 2, 3]
# first, second, third = order
# print(order)
#
# del order[0]
# print(order)

#zadanie 1 moduł 3
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_1 = lista[0:5]
# # print(lista_1)
# lista_2 = lista[5:]
# print(lista_2)
# del lista[5:]
# print(lista)
#
# # zadanie 2 moduł 3
# #
# lista_1.extend(lista_2)
# lista_1.insert(0,0)
# print(lista_1)
# lista_4 = sorted(lista_1)
# lista_4.reverse()
# print(lista_4)
#
# # zadanie 3 moduł 3
#
# zdanie = input('Podaj zdanie: \n')
# zdanie_2 = set(zdanie.lower())
# print(zdanie_2)
# zdanie_3 = list(zdanie_2)
# print(sorted(zdanie_3))
#
#
# order = [1, 2, 3]
# first, second, third = order
# #
# słownik = {'jeden': 1, 'dwa' :2, 'trzy': 3}
# print(słownik['jeden'])
#
# print('cztery' in słownik)
# print(słownik.keys())
# print(słownik.values())
# słownik['cztery'] = 4
# print(słownik.keys())
# print(słownik['cztery'])

# # zadanie 4 z modułu 3
# miesiace = dict({1:'styczen', 2:'luty', 3:'marzec', 4:'kwiecien', 5:'maj', 6:'czerwiec'})
# print(miesiace[1])
# print(miesiace[4])
#
# miesiace_pl = dict({1:'styczen', 2:'luty', 3:'marzec', 4:'kwiecien', 5:'maj', 6:'czerwiec'})
#
# months_en = dict({1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'})
#
# year = {'pl':miesiace_pl, 'en':months_en}
#
# print(year['pl'][4])

lista_a = [1, 11, 111, 1111]
lista_b = [2, 22, 222, 2222]
lista_d = [3, 33, 333, 3333]
lista_e = [4, 44, 444, 4444]
lista_a.extend(lista_b)
print(lista_a)
lista_c = sorted(lista_a)
print(lista_c)

lista_d.append(lista_e)
print(lista_d)

