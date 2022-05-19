matrix = {0:input().replace(' ',''),1:input().replace(' ',''),2:input().replace(' ',''),3:input().replace(' ',''),4:input().replace(' ','')}

for x in matrix.keys():
    if '1' in matrix[x]:
        print(abs(3 - (matrix[x].find('1')+1)) + abs(3 - (x + 1)))

