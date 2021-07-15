from datetime import datetime
def half_life(p1,p2):
    d1,d2=sorted([datetime.strptime(p1,"%Y-%m-%d"),datetime.strptime(p2,"%Y-%m-%d")])
    return (d2+(d2-d1)).strftime("%Y-%m-%d")
