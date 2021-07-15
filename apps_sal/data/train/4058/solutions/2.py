def pattern(n):
    c,p = 0,0
    t,final = '',''
    for i in range((2*n)-1):
        
        if i>=n:
            c-=1
        else:
            c+=1

        if c>9:
            temp = str(c)
            p = int(temp[-1])
        else:
            p = c

        for j in range((2*n)-1):
            if j == i or j == ((2*n)-2)-i:
                if i<n:
                    t+=str(p)
                else:
                    t+=str(p)
            else:
                t+=' '
        final += t + '\n'
        t = ''

    return final[0:-1]

