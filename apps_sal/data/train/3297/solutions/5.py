will_it_balance=lambda a,s:s.index(1)<=sum(i*a[i]for i in range(len(a)))/sum(a)<=len(s)-s[::-1].index(1)-1
