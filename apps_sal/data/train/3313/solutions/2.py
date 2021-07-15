wrap = lambda s: s if s[0] in '()' else '<span style="color: ' + {'F':'pink', 'L':'red', 'R':'green'}.get(s[0], 'orange') + '">' + s + '</span>'    

def highlight(code):
    r, last = '', ''
    
    for c in code:
        if last and c != last[-1] and not (c.isdigit() and last.isdigit()):
            r += wrap(last)
            last = ''
        last += c
                  
    return r + wrap(last)      
