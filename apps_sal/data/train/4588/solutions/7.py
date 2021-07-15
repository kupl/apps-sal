def controller(events):
    r=''
    h=o=p=0
    for c in events:
        if c=='P':
            if not o:
                o=1 if h==0 else -1
            else:p^=1
        elif c=='O':
            o=-o
        if not p:
            h+=o
            if h in(0,5):o=0
        r+=f'{h}'
    return r
