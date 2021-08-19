def winner(a, b):
    (sumodd, sumeven) = (0, 0)
    even = 0
    if a >= 1 and a <= 1000 and (b <= 1000) and (b >= 1):
        for i in range(500):
            if sumodd > a:
                return 'Bob'
            if sumeven > b:
                return 'Limak'
            even += 2
            sumeven += even
            sumodd += even - 1
    else:
        print('Enter a valid value of a and b.')


T = int(input())
mylist = []
if T >= 1 and T <= 1000:
    for i in range(T):
        (a, b) = input().split(' ')
        mylist.append([int(a), int(b)])
else:
    print('Enter a valid limit')
for i in range(T):
    print(winner(mylist[i][0], mylist[i][1]))
