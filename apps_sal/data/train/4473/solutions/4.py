from itertools import accumulate

XP=[0,0,314]
for i in range(2,170):
    XP.append(XP[-1]*(125-i//10)//100)
XP=list(accumulate(XP))

def xp_to_target_lvl(xp=-1, lvl=0):
    try: 
        if xp<0 or lvl<1: return 'Input is invalid.'
        res = XP[lvl]-xp
        return res if res>0 else f'You have already reached level {lvl}.'
    except: return 'Input is invalid.'
