def palindrome(num):
    if type(num) != int:
        return "Not valid"
    elif num < 0:
        return "Not valid"
    else:
        l = list(str(num))
        pals = []
        for i in range(len(l)):
            r_l = l[i+1:]            
            for j in range(len(r_l)):
                seq = l[i:i+1]+r_l[:j+1]
                print(seq)
                if len(seq)%2==0:
                    mid = int(len(seq)/2)
                    fr = seq[:mid]
                    bk = seq[mid:][::-1]                    
                else:
                    mid = len(seq)//2
                    fr = seq[:mid]
                    bk = seq[mid+1:][::-1]                
                if fr == bk:
                    pal = int(''.join(seq))
                    if pal%10 != 0 and pal not in pals:                        
                        pals.append(pal)
        if pals:
            return sorted(pals)
        else:
            return "No palindromes found"
                
                
          
            
              

