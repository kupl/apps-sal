def on_line(li):
    try:
        li = list(set(li))
        x1,y1 = li.pop()
        return li[0] and len(set([(y2-y1)/(x2-x1) for x2,y2 in li]))==1
    except : return len(li)<2 or len({i[0] for i in li})==1
