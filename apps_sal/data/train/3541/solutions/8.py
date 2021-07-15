def find_page_number(pages):
    p=pages[:]
    x=1
    r=[]
    while(p):
        if p[0]!=x:
            r.append(p.pop(0))
        else:
            x+=1
            p.pop(0)
    return r
