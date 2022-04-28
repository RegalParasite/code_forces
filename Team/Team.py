n = int(input())
total = 0
for x in range(n):
    problem = str(input()).replace(' ', '')
    problem = [int(a) for a in str(problem)]
    know = 0
    for i in problem:
        know += int(i)
    if know >= 2:
        total += 1

print(total)

