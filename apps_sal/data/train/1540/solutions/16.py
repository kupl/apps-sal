# cook your dish here
def check(n,k):
    return 1 if k>=n and k%n==0 else 0

def __starting_point():
    for _ in range(int(input())):
        n=int(input())
        k=int(input())
        if check(n,k):
            print("YES")
        else:
            print("NO")
__starting_point()
