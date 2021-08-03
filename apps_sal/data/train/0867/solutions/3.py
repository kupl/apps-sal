# cook your dish here
import math
for i in range(int(input())):
    test_list = list(map(int, input().split()))
    y = test_list.pop(0)
    print(math.ceil(sum(test_list) / y))
