places = str(input()).split(' ')
score = str(input()).split(' ')

score_places = int(score[int(places[-1])-1])
total = 0

for i in score:
    if i != '0' and int(i) >= score_places:

        total += 1
print(total)
