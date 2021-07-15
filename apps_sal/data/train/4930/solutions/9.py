from itertools import combinations as c
def find_zero_sum_groups(arr, n):
    a=sorted(set(arr))
    ans=[]
    for i in c(a,n):
        if sum(i)==0:
            ans.append(list(i))
    if not arr: return 'No elements to combine'
    if not ans: return 'No combinations'
    if len(ans)==1: return ans[0]
    return ans
