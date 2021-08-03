t = int(input())
for i in range(t):
    s, w1, w2, w3 = list(map(int, input().split()))
    list1 = []
    list1.append(w1)
    list1.append(w2)
    list1.append(w3)
    list1.sort()
    if((list1[0] + list1[1] + list1[2]) <= s):
        print(1)
    elif((list1[0] + list1[1]) <= s):
        print(2)
    else:
        print(3)
