import math
for i in range(int(input())):
    l = [2, 3, 1]
    num = int(input())
    if math.ceil(math.log2(num)) == math.floor(math.log2(num)):
        print(-1)
        continue
    elif num == 1:
        print(1)
        continue
    elif num == 3:
        print("1 3 2")
        continue
    else:
        for i in range(4, num + 1):
            if math.ceil(math.log2(i)) == math.floor(math.log2(i)):
                if i not in l:
                    l.append(i + 1)
                    l.append(i)
            else:
                if i not in l:
                    l.append(i)
    print(' '.join(map(str, l)))
