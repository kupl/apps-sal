test = int(input())
for i in range(test):
    flavor = int(input())
    rate = input()
    gaf = input()
    gaf = gaf.split()
    gaf = [int(x) for x in gaf]
    rate = rate.split()
    rate = [int(x) for x in rate]
    rate.sort()
    c = gaf[0] - gaf[1]
    sum = rate[0] * c
    t = True
    if gaf[0] < gaf[1]:
        t = False
    j = 0
    while j < gaf[1] and t:
        sum = sum + rate[j]
        j = j + 1
    if t:
        print(sum)
    else:
        print('Not Possible')
