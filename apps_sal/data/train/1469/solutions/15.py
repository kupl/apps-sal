try:
    # def solve(n):
    #     res=""
    #     while(n!=0):
    #         if(n%2==0):
    #             res="0"+res
    #         else:
    #             res="1"+res
    #         n>>=1
    #     return res
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = 2
        for i in range(n):
            z = c
            for j in range(n):
                print(z, end="")
                z += 1
            c += 1
            print()
except EOFError:
    pass
