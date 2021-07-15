# cook your dish here
try:
    n=int(input())
    for i in range(n):
        a=input()
        
        print(int(a, 16))
except EOFError as e:
    pass
