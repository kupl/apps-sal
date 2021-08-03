import math


def movie(crd, tkt, pcnt):

    tktCnt = TotalA = TotalB = 0

    while(math.ceil(TotalB) >= TotalA):
        tktCnt += 1
        TotalA = tkt * tktCnt
        TotalB = crd + tkt * ((pcnt * ((pcnt**tktCnt) - 1)) / (pcnt - 1))

    return(tktCnt)
