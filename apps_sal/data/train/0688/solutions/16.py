val = int(input())
for i in range(val):
    p = input()
    p = str(p)
    b = p.count('10') + p.count('01')

    if(b <= 2):
        print("uniform")
    else:
        print("non-uniform")
