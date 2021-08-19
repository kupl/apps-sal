A, B = [int(i) for i in input().split()]
counter = 0
for x in range(1, A + 1):
    num = x**2 + B
    counter += (int(num**0.5) - x)
    # print(x,num)
print(counter)
