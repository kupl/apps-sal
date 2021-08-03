# cook your dish here
T = int(input())
for _ in range(T):
    X = int(input())
    ans = X.bit_length()
    if 2**(ans - 1) == X:
        print(2**(ans - 1))
        continue
    print(2**(ans))
