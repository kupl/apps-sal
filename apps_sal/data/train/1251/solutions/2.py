n = int(input())
s = list(map(str, input().split()))
m = int(input())
dic = {}
for i in range(m):
    a, b, c = list(map(str, input().split()))
    c = int(c)
    dic[(a, b)] = c

t = int(input())
for i in range(t):
    x = list(map(str, input().split()))
    y = len(x)
    if int(x[0]) == 1 and x[1] in s:
        print("0")
    elif int(x[0]) == 1:
        print("ERROR")
    elif x[1] == x[y - 1]:
        print("ERROR")
    else:
        if int(x[0]) > n:
            print("ERROR")
        else:
            flag = 1
            ans = 0
            dic2 = {}
            for j in range(1, len(x)):
                if x[j] in dic2:
                    dic2[x[j]] += 1
                else:
                    dic2[x[j]] = 1
            for j in dic2:
                if dic2[j] > 1:
                    flag = 0
                    break
            if flag == 1:
                for j in range(1, len(x) - 1):
                    if (x[j], x[j + 1]) in dic:
                        ans += dic[(x[j], x[j + 1])]
                    else:
                        flag = 0
                        break
            if flag == 0:
                print("ERROR")
            else:
                print(ans)
