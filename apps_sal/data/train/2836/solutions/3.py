from fractions import Fraction

def find_screen_height(width, ratio): 
    ratio = ratio.replace(":","/")
    ratio = float(sum(Fraction(s) for s in ratio.split()))
    return "{}x{}".format(width, int(width/ratio))
