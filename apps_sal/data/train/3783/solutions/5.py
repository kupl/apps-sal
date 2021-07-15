def frame(t, c):
    m = len(max(t,key=len))
    return c*(m+4) + '\n' + "\n".join([f'{c} {i:<{m}} {c}' for i in t]) + '\n' + c*(m+4)
