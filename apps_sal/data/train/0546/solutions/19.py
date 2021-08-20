def bitsoncount(x):
    return bin(x).count('1')


for t in range(int(input())):
    x = int(input())
    if x == 0:
        print(0)
    else:
        print(bitsoncount(x) - 1)
