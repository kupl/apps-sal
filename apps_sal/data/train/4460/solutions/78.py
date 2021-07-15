def whatday(n):
    l=['','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Wrong, please enter a number between 1 and 7']
    return l[n] if 0<n<8 else l[8]
