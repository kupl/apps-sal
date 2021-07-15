watch_pyramid_from_the_side=lambda c:'\n'.join([(j*(i*2+1)).center(len(c)*2-1) for i,j in enumerate(c[::-1])]) if c else c
count_visible_characters_of_the_pyramid=lambda c:(len(c)*2-1)**2 if c else -1
count_all_characters_of_the_pyramid=lambda c:sum(k**2 for k in range(1,len(c)*2,2)) if c else -1
def watch_pyramid_from_above(c):
    above = [''.join(j).replace(' ',(c+c[:-1][::-1])[i]) for i,j in enumerate(zip(*watch_pyramid_from_the_side(c).splitlines()))] if c else []
    return '\n'.join([''.join(i) for i in list(zip(*above))[::-1][:-1]+list(zip(*above))]) if c else c
