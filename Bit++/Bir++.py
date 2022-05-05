n = int(input())
total = 0
for x in range(n):
    x = input()
    if '+' in x:
        total += 1
    elif '-' in x:
        total -= 1 

print(total)
