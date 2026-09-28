a = int(input())
m = (a//60)%60
h = a//60//60
s = a%60
h1, m1, s1 = '0' + str(h), '0' + str(m), '0' + str(s)
print(f'{h1[-2:]}:{m1[-2:]}:{s1[-2:]}')
