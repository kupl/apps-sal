# cook your dish here
num = int(input())

mat = [[-1 for i in range(num * 2 - 1)]for j in range(num * 2 - 1)]
cs = 0
rs = 0

re = len(mat) - 1
ce = len(mat) - 1


while num:

    t = num * 2 - 1

    for i in range(cs, ce + 1):
        mat[rs][i] = num
        mat[re][i] = num

    for j in range(rs, re):
        mat[j][cs] = num
        mat[j][ce] = num

    num -= 1
    rs += 1
    cs += 1
    re -= 1
    ce -= 1


for i in mat:
    print(*i)
