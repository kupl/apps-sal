# cook your dish here
for _ in range(int(input())):
    n = int(input())
    ingredients = list(map(int, input().split(" ")))
    ls = [ingredients[0]]
    count = []
    index = []
    c = 1
    flag = 1
    for i in range(1, n):
        if ingredients[i] == ls[-1]:
            c = c + 1
        else:
            if ingredients[i] in ls:
                flag = 0
                break
            index.append(i)
            ls.append(ingredients[i])
            if c in count:
                flag = 0
                break
            count.append(c)
            c = 1
    if c in count or flag == 0:
        print("NO")
        continue
    print("YES")

    # for i in range(n):
