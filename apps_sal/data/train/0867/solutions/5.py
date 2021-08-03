# cook your dish here
import math
for i in range(int(input())):
    li = list(map(int, input().split()))
    y = li.pop(0)
    print(math.ceil(sum(li) / y))
