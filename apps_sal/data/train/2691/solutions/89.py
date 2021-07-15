def solve(s):
    char='abcdefghijklmnopqrstuvwxyz'
    ans=''
    answer=[]
    for i in s:
        if i in char:
            ans+=' '
        else:
            ans+=i
    ans = ans.split(' ')
    while ans.count('')!=0:
        ans.remove('')
    for i in ans:
        i = int(i)
        answer.append(i)
    return max(answer)

