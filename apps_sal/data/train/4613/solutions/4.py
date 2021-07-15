def bitAdd(b, co):
    if b == '00':
        if co: 
            return '1', False
        else:
            return '0', False
        
    if b in ['01', '10']: 
        if co: 
            return '0', True
        else:
            return '1', False
        
    if b == '11':
        if co: 
            return '1', True
        else:
            return '0', True
        

def add(a, b):
    if len(a) < len(b):
        a = ((len(b)-len(a))*'0')+a
    else:
        b = ((len(a)-len(b))*'0')+b
    #
    bits=[i+j for i, j in zip(reversed(a),reversed(b))]
    co = False
    ans = ['' for i in range(len(a))]
    for i,b in enumerate(bits):
        ans[i], co = bitAdd(b, co)
    #
    if co: ans.append('1')
    ans = ''.join(reversed(ans)).lstrip('0')
    #
    if ans == '': return '0'
    return ans
