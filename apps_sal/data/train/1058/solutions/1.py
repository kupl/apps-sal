t = int(input())
for i in range(t):
    n = input()
    l = len(n)
    list1 = list(n)
    str1 = ''
    for j in range(l):
        str1 += str(int(list1[j]) - 2)
    print(str1)
