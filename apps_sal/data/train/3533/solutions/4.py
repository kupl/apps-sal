def de_nico(key,msg):
    result = ''
    counter = -1
    while len(result) < len(msg):
        counter += 1
        for i in [sorted(key).index(c) for c in key]:
            try:
                result += msg[i+counter*len(key)]
            except:
                continue
    return result.strip()

