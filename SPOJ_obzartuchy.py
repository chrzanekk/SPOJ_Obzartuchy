import math
testy = int(input()) 
for i in range(testy):
    N = int(input()) 
    M = int(input()) 
    ile = 0
    for j in range(N):
        t = int(input()) 
        ile += (86400/t)
    wynik = ile/M
    print(math.ceil(wynik))
