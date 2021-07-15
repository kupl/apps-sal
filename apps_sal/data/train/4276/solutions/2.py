def solution(n):
    #your code here
    x=divmod(n,.5)
    if x[1] <.25:
        return x[0]*.5
    else:
        return x[0]/2 + .5

