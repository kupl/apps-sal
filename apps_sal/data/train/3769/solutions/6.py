def execute(codes):
    Nums = '0123456789'
    code = ''
    t = 0
    c = 0
    while t < len(codes):
        Char = 0
        c = 1
        if t < len(codes) - 1:
            for g in codes[t + 1:]:
                if g in Nums:
                    Char += 1
                else:
                    break
                c = int(codes[t + 1:t + Char + 1])
        code += codes[t] * c
        t += 1 + Char
    Xs = 0
    Ys = 0
    X = []
    Y = []
    Ymin = 0
    Step = [[0, 0]]
    Rotation = 0
    Arr = []
    Out = ''
    for i in range(len(code)):
        if code[i] == 'L':
            Rotation += 90
        elif code[i] == 'R':
            Rotation += -90
        if Rotation > 180:
            while Rotation > 180:
                Rotation += -360
        elif Rotation < -180:
            while Rotation < -180:
                Rotation += 360
        if code[i] == 'F':
            if Rotation == 0:
                Xs += 1
            elif Rotation == -180 or Rotation == 180:
                Xs += -1
            elif Rotation == 90:
                Ys += 1
            elif Rotation == -90:
                Ys += -1
            Step.append([Xs, Ys])
    for u in Step:
        X.append(u[0])
        Y.append(u[1])
    for j in range(len(Step)):
        Step[j][0] = Step[j][0] + min(X) * -1
        Step[j][1] = Step[j][1] + min(Y) * -1
    for k in range(max(Y) - min(Y) + 1):
        Arr.append([' '] * (max(X) - min(X) + 1))
    for l in Step:
        Arr[max(Y) - min(Y) - l[1]][l[0]] = '*'
    for n in range(len(Arr)):
        for p in range(max(X) - min(X) + 1):
            Out += Arr[n][p]
        Out += '\r\n'
    Out = Out[:-2]
    return Out
