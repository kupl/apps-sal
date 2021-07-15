def passer_rating(att, yds, comp, td, ints):
    a = ((comp/att)-0.3)*5 ; a = min(a, 2.375) ; a = max(a, 0)
    b = ((yds/att)-3)*0.25 ; b = min(b, 2.375) ; b = max(b, 0)
    c = (td/att)*20 ; c = min(c, 2.375) ; c = max(c, 0)
    d = 2.375 - ((ints/att)*25) ; d = min(d, 2.375) ; d = max(d, 0)
    
    return round(((a+b+c+d)/6)*100,1)

