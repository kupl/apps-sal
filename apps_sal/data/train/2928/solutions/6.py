alphabet_war=lambda s,f=(lambda x,y:sum(y.find(e)+1 for e in x)):(lambda a,b:"Let's fight again!" if a==b else '{} side wins!'.format(['Left','Right'][b>a]))(f(s,'sbpw'),f(s,'zdqm'))
