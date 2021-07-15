def pattern(n,m=1,l=1,*args):
    if n < 1:return ''
    m = max(1,m)
    li, mid, r = ['1'+' '*((n*2-1)-2)+'1'+(' '*((n*2-1)-2)+'1')*(m-1)],1,(n*2-1)-2-2
    for i in range(2, n + 1):
        li.append(' '*(i-1)+f"{' '*mid}".join([str(i%10)+' '*r+(str(i%10)if i!=n else '')for o in range(m)])+' '*(i-1))
        r -= 2 ; mid += 2
    li = li + li[:-1][::-1]
    well = li.copy()
    return "\n".join(li + ["\n".join(well[1:]) for i in range(l-1)])
