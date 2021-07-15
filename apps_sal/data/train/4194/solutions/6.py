def next_version(version):
    if "." not in version: return str(int(version) + 1)
    v = [i for i in version.split(".")]
    minor_version = False
    
    for index in reversed(list(range(len(v)))):
        if index == len(v)-1 :
            if int(v[index]) < 9 :
                v[index] = str(int(v[index]) + 1)
                return ".".join(v)
            else:
                minor_version = True
                v[index] = "0"
                continue                
            
        if minor_version:
            v[index] = str(int(v[index]) + 1)
                        
            if int(v[index]) != 10 or index == 0 :
                return ".".join(v)
            else:    
                minor_version = True
                v[index] = "0"
                continue

