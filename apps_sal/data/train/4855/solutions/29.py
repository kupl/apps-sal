vert_mirror = lambda strng: '\n'.join(i[::-1] for i in strng.split())
hor_mirror = lambda strng: '\n'.join(strng.split()[::-1])
oper = lambda fct, s: fct(s)
