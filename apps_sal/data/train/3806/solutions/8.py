import _thread
import time

def black_and_white(height, width, compressed):
    actual=width
    resu=[]
    lev=[]
    isblack=True
    for x in compressed:
#         if lev == [] and x%2==0:
#             lev.append(0)
        while x >= actual:
            x-=actual
            lev.append(actual)
            if not len(lev) % 2 == 0:
                lev.append(0)
            actual=width
            resu.append(lev)
            lev=[]
            if not isblack:
                lev.append(0)
        if x < actual:
            actual-=x
            lev.append(x)
            isblack=not isblack
#     print('=============RESULT================')
    return(resu)

