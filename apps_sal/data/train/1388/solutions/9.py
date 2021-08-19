# cook your dish here
for i in range(int(input())):
    x = int(input())
    l = [250000, 500000, 750000, 1000000, 1250000, 1500000]
    l1 = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
    count = 0
    if x <= l[0]:
        print(x)
    else:
        for i in range(1, len(l)):
            if x <= l[i]:
                p = x - l[i - 1]
                count = count + (p * l1[i - 1])
                break
            else:
                p = l[i] - l[i - 1]
                count = (l1[i - 1] * p) + count
        else:
            p = x - l[len(l) - 1]
            count = p * l1[len(l1) - 1] + count
        print(int(x - count))
