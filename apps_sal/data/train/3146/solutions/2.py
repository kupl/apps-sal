import re
def to_utf8_binary(string):
    s=''
    for c in string:
        r=bin(ord(c))[2:]
        if len(r)<8:
            s+='0'+r.zfill(7)
        elif len(r)<12:
            t=r.zfill(11)
            s+='110{}10{}'.format(t[:5],t[5:])
        elif len(r)<17:
            t=r.zfill(16)
            s+='1110{}10{}10{}'.format(t[:4],t[4:10],t[10:])
        elif len(r)<22:
            t=r.zfill(21)
            s+='11110{}10{}10{}10{}'.format(t[:3],t[3:9],t[9:15],t[15:])
    return s

def from_utf8_binary(bitstring):
    s=''
    for i in re.findall('0([01]{7})|110([01]{5})10([01]{6})|1110([01]{4})10([01]{6})10([01]{6})|11110([01]{3})10([01]{6})10([01]{6})10([01]{6})',bitstring):
        s+=chr(int(''.join(i),2))
    return s        
