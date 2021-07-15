def queue(q,pos):
    time = 0
    while True:
        time += 1
        if q[0] == 1:
            if pos: q.pop(0)
            else:   return time
        else:
            q.append(q.pop(0) - 1)
        pos = pos - 1 if pos  else len(q) - 1

