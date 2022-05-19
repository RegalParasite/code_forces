string1 = input().lower()
string2 = input().lower()
total1 = 0
total2 = 0
letters = 'abcdefghijklmnopqrstuvwxyz'

if 1 == 1:
    for x in string1:
        total1 += letters.find(x)
    for x in string2:
        total2 += letters.find(x)
if total1 > total2:
    print(1)

if total2 > total1:
    print(-1)

if total1 == total2:
    print(0)
