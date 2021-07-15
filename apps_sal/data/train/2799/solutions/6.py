def beasts(h, t):
    O, H = 5*t-h, h-2*t
    if O>=O%3>=0<=H%3<=H: return [O//3, H//3]
    else: return "No solutions"
