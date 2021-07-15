import random

def love_language(partner, weeks):
    rst = [0,0,0,0,0]
    for i in range (0, weeks*7):
        if(partner.response(LOVE_LANGUAGES[i%5]) == 'positive'):
            rst[i%5]+=1
    return LOVE_LANGUAGES[rst.index(max(rst))]

