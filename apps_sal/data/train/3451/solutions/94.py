def k_color_code(a,b):
    i = 0
    j = 0
    if(a.lower() == 'r'):
        i = 1
    if(a.lower() == 'b'):
        i = 0.1
    if(a.lower() == 'g'):
        i = 0.01
    if(b.lower() == 'r'):
        j = 1
    if(b.lower() == 'b'):
        j = 0.1
    if(b.lower() == 'g'):
        j = 0.01    
    return i + j

def k_color(k_code):

    if k_code == 0.02:
        return 'g'
    elif k_code == 0.2:
        return 'b'
    elif k_code == 2:
        return 'r'
    elif k_code == 1.01:
        return 'b'
    elif k_code == 1.1:
        return 'g'
    elif k_code == 0.11:
        return 'r'
    elif k_code == 0.11:
        return 'r'
    else:
        return 'n'

def new_row(row):
    s = row
    ps = ""
    x = s
    for i in range(0,len(x)):
        if i + 1 != len(x):
            ps += k_color(k_color_code(x[i],x[i+1]))
        else:
            break
    x = ps
    return x

def triangle(row):
    s = row
    while(len(s) != 1):
        s = new_row(s)
    return s.upper()


