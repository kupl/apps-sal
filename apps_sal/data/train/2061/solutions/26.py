exec("a=list(map(int,input().split()));g=sum(a[::2])-max(a[::2]);h=sum(a[1::2])-max(a[1::2]);print(max([abs(g),abs(h)])+(g*(g-1)and g==h));" * int(input()))
