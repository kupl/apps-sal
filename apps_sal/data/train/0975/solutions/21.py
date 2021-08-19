a = int(input())
while a != 0:
    (b, c, d, e) = map(int, input().split())
    mylist1 = list()
    mylist2 = list()
    if d > 0:
        mylist1 = list(map(int, input().split()))
    if e > 0:
        mylist2 = list(map(int, input().split()))
    mylist2.extend(mylist1)
    list1 = list(set(mylist2))
    if b - len(list1) >= c:
        print(c)
    else:
        print(b - len(list1))
    a -= 1
