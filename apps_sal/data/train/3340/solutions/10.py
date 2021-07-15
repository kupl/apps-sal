def sharkovsky(a,b):
    
    def Answer(n):
        con = True
        p = 0
        while con == True:
            if n %2!=0:
                ans =  (p,n)
                con = False
            else:
                n= n /2
                p +=1
        return ans
    ans_a = Answer(a)    
    ans_b = Answer(b) 
    
    if ans_a[1]==1 and ans_b[1]!=1:
        return False
    elif ans_a[1]!=1 and ans_b[1]==1:
        return True
    elif ans_a[1]==1 and ans_b[1]==1:
        return ans_a[0]>ans_b[0]
    else:
        if ans_a[0]>ans_b[0]:
            return False
        elif ans_a[0]<ans_b[0]:
            return True
        else:
            return ans_a[1]<ans_b[1]

