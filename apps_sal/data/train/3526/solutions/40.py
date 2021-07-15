import re

def any_arrows(arrows):
    damaged_arrows = []
    good_arrows = []
    
    sorted_arrows = arrows.copy()
    sorted_arrows.sort(key=lambda arrow: arrow.get('range') if arrow.get('range') else 0, reverse=True)
    
    print(sorted_arrows)
    
    for arrow in sorted_arrows:
        if arrow.get('damaged'):
            damaged_arrows.append(arrow)
        else:
            good_arrows.append(arrow)
            
    print(damaged_arrows)
    print(good_arrows)
    
    return len(good_arrows) > 0
    

