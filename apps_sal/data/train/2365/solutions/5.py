import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    def ok():
        if len(ans)<n:return False
        for r,si in enumerate(sii,2):
            s=ss[si]
            cur=set(ans[r-len(s):r])
            if s!=cur:return False
        return True

    for _ in range(II()):
        n=II()
        ee=[[n**2]*n for _ in range(n)]
        for ei in range(n):ee[ei][ei]=0
        ss=[set(LI()[1:]) for _ in range(n-1)]
        for a0 in range(1,n+1):
            used=set([a0])
            ans=[a0]
            sii=[]
            for _ in range(n-1):
                nxt=[]
                for si,s in enumerate(ss):
                    cur=s-used
                    if len(cur)==1:
                        for a in cur:nxt.append(a)
                        sii.append(si)
                if len(nxt)!=1:break
                ans.append(nxt[0])
                used.add(nxt[0])
            if ok():break
        print(*ans)

main()
