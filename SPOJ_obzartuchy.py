import math
testy = int(input()) #test count
for i in range(testy):
    n = int(input()) #ilosc obzartuchow
    m = int(input()) #ilosc ciastek
    summary = 0
    for j in range(n):
        time = int(input()) #czas zjadania ciastek w sekundach
        how_much = 86400/time #ile ciastek zjedza w ciagu 24h
        summary += how_much
    boxes = round(summary/m,2)
    print(math.ceil(boxes))
