import math
def scroller(text, amp, period):
    l = lambda i, c: ' '*(amp+i) + c + "\n"
    return (''.join([l(round(amp * math.sin(2*math.pi*(i/period))), text[i]) for i in range(len(text))]))[:-1]
