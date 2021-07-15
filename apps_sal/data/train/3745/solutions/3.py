def condi_helper(message, init_key, shift, mode):
    key = sorted(set(init_key), key=init_key.index)
    key += sorted(set('abcdefghijklmnopqrstuvwxyz') - set(init_key))
    
    result=[]
    for char in message:
        if char in key:
            idx = key.index(char)
            new = (idx + mode * shift) % 26
            result.append(key[new])
            if mode == 1:
                shift = idx + 1
            else:
                shift = new + 1
        else:
            result.append(char)
    
    return ''.join(result)

encode = lambda msg, key, sh: condi_helper(msg, key, sh, 1)
decode = lambda msg, key, sh: condi_helper(msg, key, sh, -1)
