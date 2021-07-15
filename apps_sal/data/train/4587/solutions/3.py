import re
def range_parser(string):
    r=[]
    for i in [i.strip() for i in string.split(',')]:
        if bool(re.match('^\d+$',i)):
            r.append(int(i))
        elif bool(re.match('^\d+-\d+$',i)):
            x=i.split('-')
            r.extend([j for j in range(int(x[0]),int(x[1])+1)])
        elif bool(re.match('^\d+-\d+:\d+$',i)):
            x=i.split('-')
            y=x[1].split(':')
            r.extend([j for j in range(int(x[0]),int(y[0])+1,int(y[1]))])
    print(r)
    return r
