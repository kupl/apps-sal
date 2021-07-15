class Arrow:
    def __init__(self, range = 5, damaged = False):
        self.range = range
        self.damaged = damaged

def any_arrows(arrows):
    quiver = []    
    for arrow in arrows:
        if 'range' in arrow and 'damaged' in arrow:
            quiver.append(Arrow(arrow.get('range'), arrow.get('damaged')))
        elif 'range' in arrow:
            quiver.append(Arrow(range = arrow.get('range')))
        elif 'damaged' in arrow:
            quiver.append(Arrow(damaged = arrow.get('damaged')))
        else:
            quiver.append(Arrow())
    return False in [x.damaged for x in quiver]
