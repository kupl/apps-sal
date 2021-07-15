import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__



def go():
    # n = int(input())
    n,m = list(map(int, input().split()))
    c=''.join(input() for _ in range(n))
    s=''.join(input() for _ in range(n))

    nm = n * m
    done = [False] * nm
    groups = [None] * nm
    phase = [-1]*nm

    def step(pos,direct=None):
        if direct is None:
            direct=s[pos]
        if direct=='U':
            return pos-m
        if direct=='D':
            return pos+m
        if direct=='L':
            return pos-1
        if direct=='R':
            return pos+1

    cyc_len={}

    for i in range(nm):
        if not done[i]:
            same = {}
            pos=0
            cur=i
            group=-1
            pcur=None
            while cur not in same:
                if groups[cur] is not None:
                    group=groups[cur]
                    pcur=pos+phase[cur]
                    break
                same[cur]=pos
                done[cur]=True
                cur=step(cur)
                pos+=1
            else:
                group=cur
                cyc_len[group]=len(same)-same[cur]
                pcur=pos

            for ss,pos in list(same.items()):
                groups[ss]=group
                phase[ss]=(pcur-pos)%cyc_len[group]

    blacks =  len(set((pp,gg)for cc,pp,gg in zip(c,phase,groups) if cc=='0'))
    # print('ppp',phase)
    # print(groups)
    # print('--',cyc_len)

    return f'{sum(cyc_len.values())} {blacks}'

# x,s = map(int,input().split())
t = int(input())
# t = 1
ans = []
for _ in range(t):
    # print(go())
    ans.append(str(go()))
#
print('\n'.join(ans))

