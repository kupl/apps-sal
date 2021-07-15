min_sum=lambda a:a.sort()or sum(a[i]*a[-i-1]for i in range(len(a)//2))
