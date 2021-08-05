# cook your dish here
for i in range(int(input())):
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst1.sort()
    lst2.sort()
    lst12 = []
    lst21 = []
    for i in range(n):
        lst12.append(lst1[i])
        lst12.append(lst2[i])
        lst21.append(lst2[i])
        lst21.append(lst1[i])
    # print(lst12)
    # print(lst21)
    lst3 = lst1 + lst2
    lst3.sort()
    if(lst12 == lst3 or lst21 == lst3):
        print("YES")
    else:
        print("NO")
