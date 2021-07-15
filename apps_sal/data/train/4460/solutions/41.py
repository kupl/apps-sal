from calendar import day_name
def whatday(num):
    d={}
    c=2
    for i in list(day_name):
        if i=='Sunday':
            d[1]=i
        else:
            d[c]=i
        c+=1
    return d.get(num,'Wrong, please enter a number between 1 and 7')
