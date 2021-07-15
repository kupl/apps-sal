from math import log
def find_ball(scales, ball_count):
    count=2 if ball_count <=9 else int(log(ball_count, 3))+1 if str(log(ball_count, 3))[-2:]!=".0" else int(log(ball_count, 3))
    res=[i for i in range(ball_count)]    
    for i in range(count):
        if len(res)<=2: break
        flag=scales.get_weight(res[:(len(res)+1)//3], res[(len(res))-(len(res)+1)//3:])
        if flag==-1: 
            res=res[:(len(res)+1)//3] 
        elif flag==1:
            res=res[(len(res))-(len(res)+1)//3:]
        elif flag==0:
            res=res[(len(res)+1)//3:(len(res))-(len(res)+1)//3] 
    if len(res)==1: return res[0]
    return res[0] if scales.get_weight(res[:1], res[1:])==-1 else res[1]
