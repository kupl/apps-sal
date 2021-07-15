import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n = II()
    aa = LI()
    # できる数列にインデックスがかかれるときの最大値の底(bottom)
    bot = []
    mx = 0
    for i, a in enumerate(aa):
        if a > mx:
            bot.append((mx, i))
            mx = a
    #print(bot)
    aa.sort()
    ans = [0] * n
    j = n
    s = 0
    fin=0
    for mx, i in bot[::-1]:
        while j > 0 and aa[j - 1] > mx:
            j -= 1
            s += aa[j]
        ans[i]=s-(n-j)*mx-fin
        # print(mx,i,j,s,fin,ans)
        fin+=ans[i]
    print(*ans,sep="\n")

main()

