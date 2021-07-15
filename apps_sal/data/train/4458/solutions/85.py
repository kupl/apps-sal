def time_correct(t):
    if len(str(t))==0:
        return ""
    time = str(t).split(':')
    for i in time:
        if len(i)!=2:
          return None  
    if len(time) != 3:
        return None
    else:
        try:
            t = [int(i) for i in time]
        except Exception:
            return None
        while t[2]>59:
            t[1]+=1
            t[2]-=60
        while t[1]>59:
            t[0]+=1
            t[1]-=60
        t[0]=t[0]%24
        t = [str(i) for i in t]
        for i in range(3):
            if len(t[i])==1:
                t[i] = "0"+t[i]
        ans = ':'.join(t)
        return ans
            
            

