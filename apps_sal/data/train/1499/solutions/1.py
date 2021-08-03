# cook your dish here
# code by RAJ BHAVSAR
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def row_helper(data, s, p, q):
    t1 = 0
    for i in range(len(data[0])):
        if(data[0][i] != int(s[i])):
            t1 += min(p, q)
    return t1


def col_helper(data, s, p, q):
    t1 = 0
    for i in range(len(data)):
        if(data[i][0] != int(s[i])):
            t1 += min(p, q)
    return t1


for _ in range(int(input())):
    row, col = get_ints()
    data = []
    for i in range(row):
        data.append(get_list())
    s = get_string()
    p, q = get_ints()
    if(row == 1):
        print(row_helper(data, s, p, q))
    else:
        if(col == 1):
            print(col_helper(data, s, p, q))
        else:
            ans = 0
            i = 0
            while(i < row):
                temp = []
                x, y = i, 0
                while(x >= 0 and y < col):
                    temp.append(data[x][y])
                    x -= 1
                    y += 1
                t1 = 0
                for l in temp:
                    if(l != int(s[i])):
                        t1 += p
                t2 = q
                for l in temp:
                    if(l == int(s[i])):
                        t2 += p
                ans += min(t1, t2)
                i += 1
            loop = i
            i -= 1
            j = 1
            while(j < col):
                temp = []
                x, y = i, j
                while(y < col and x >= 0):
                    temp.append(data[x][y])
                    y += 1
                    x -= 1
                t1 = 0
                for l in temp:
                    if(l != int(s[loop])):
                        t1 += p
                t2 = q
                for l in temp:
                    if(l == int(s[loop])):
                        t2 += p
                ans += min(t1, t2)
                j += 1
                loop += 1
            print(ans)
