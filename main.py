import math as ma

for i in range(1,100):
    j = 1
    flag = 1
    while j <= ma.sqrt(i):
        if (i % j == 0) & (j != 1):
            flag = 0
            break
        j += 1
    if flag:
        print(str(i) + ' ')
