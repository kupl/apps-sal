# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    str1 = input()
    str3 = ""
    for i in range(0, n, 4):
        str2 = str1[i] + str1[i + 1] + str1[i + 2] + str1[i + 3]
        l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
        for j in str2:
            if j == '0':
                l1 = l1[:int(len(l1) / 2)]
            else:
                l1 = l1[int(len(l1) / 2):]
            # print(l1)
        str3 += l1[0]
    print(str3)

    t = t - 1
