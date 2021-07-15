def cal(s):
    ts =  0
    for i in s: 
        c, t = i, 0
        if '/' in i: 
            f = i.find('/')
            c = i.replace(i[f-1:f+1], 'X')
        for v in c: 
            if v == 'X': t += 10
            else: t += int(v)
        ts += t
    return ts

def bowling_score(frames):
    frames = frames.split()
    r = []
    for i in range(len(frames)):
        if i == 9: 
            r.append(frames[i])
            continue
        elif frames[i][0] == 'X':
            r.append(''.join(frames[i: i+3])[:3])
        elif '/' in frames[i]:
            r.append(''.join(frames[i: i+2])[:3] )
        
        else: 
            r.append(frames[i])
    return cal(r)
