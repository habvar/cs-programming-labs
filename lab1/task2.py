a, b = float(input()), float(input())
print(f'Площадь: {a*b}')
print(f'Периметр: {a*2 + b*2}')

a = int(input())
m = (a//60)%60
h = a//60//60
s = a%60
h1, m1, s1 = '0' + str(h), '0' + str(m), '0' + str(s)
print(f'{h1[-2:]}:{m1[-2:]}:{s1[-2:]}')

km, l_100km, l_1 = float(input()), float(input()), float(input())
print(f'Топливо: {(km/100) * l_100km} л' )
print(f'Стоимость: {((km/100) * l_100km) *l_1} руб')