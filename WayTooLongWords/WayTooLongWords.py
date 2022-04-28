long = int(input())

for x in range(long):
    word = str(input())
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)
