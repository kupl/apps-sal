def charCheck(text, mx, spaces):
    return (lambda txt: [len(txt) <= mx, txt[:mx]])([text.replace(' ', ''), text][spaces])
