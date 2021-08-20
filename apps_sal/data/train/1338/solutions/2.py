list1 = list(map(float, input().split()))
for i in range(1, len(list1) - 1, 2):
    print('{:.2f}'.format(list1[i] * 10 ** list1[i + 1]))
