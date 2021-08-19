# cook your dish here
for _ in range(int(input())):
    n = int(input())
    seq, ind = list(map(int, input().split())), []
    seq.insert(0, 0)
    count, sum_ = 0, 0
    for i in range(1, n + 1):
        if (seq[i] >= 0):
            count += 1
            sum_ += seq[i]
    for i in range(1, count + 1):
        if (seq[i] < 0):
            ind.append(i)
    for i in range(count + 1, n + 1):
        if (seq[i] >= 0):
            ind.append(i)
    print(sum_)
    print(len(ind), end=" ")
    for i in ind:
        print(i, end=" ")
    print()
