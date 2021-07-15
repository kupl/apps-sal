alphabet_war=lambda f: (lambda r: "Let's fight again!" if not r else "Left side wins!" if r>0 else "Right side wins!")(sum("mqdz sbpw".index(l)-4 if l in "mqdzsbpw" else 0 for l in f))
