n,k = list(map(int, input().split()))
s = list(map(int,input().split()))
_sum = sum(s)
if( _sum % k != 0):
    print("No")
    return
V = _sum // k

idx = 0
current_val = 0
count = 0
ans = []
while idx < len(s):
    current_val += s[idx]
    count+=1
    if(current_val > V):
        print("No")
        return
    elif(current_val == V):
        ans.append(count)
        count = 0
        current_val = 0
    idx+=1
print("Yes")
print(' '.join(list(map(str,ans))))

