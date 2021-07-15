def select_hill(hills):
    m = hills.index(max(hills))
    if m==0 or m==len(hills)-1 :
        return 1
    else:
	    return 1 + min(select_hill(hills[:m]),select_hill(hills[m + 1:]))
    

t = int(input())
for _ in range(t):
    n = int(input())
    hills = list(map(int,input().split()))
    print(select_hill(hills))
