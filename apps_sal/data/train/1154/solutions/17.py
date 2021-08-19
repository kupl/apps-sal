N = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for i in list2:
    if list1.count(i) != list2.count(i):
        print(i)
        break
