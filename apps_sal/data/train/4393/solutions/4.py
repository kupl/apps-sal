from collections import Counter as Cnt

repeat_sum = lambda l: sum(k for k,v in Cnt([e for ll in l for e in set(ll)]).items() if v>1)

