pattern=lambda n,x=1,y=1,*args: "\n".join((lambda h: h+(["\n".join(h[1:]) for k in range(1,y)]))([(lambda r: "".join(r)+"".join(["".join(r[1:]) for j in range(1,x)]))([" "]*(i-1)+[str(i%10)]+[" "]*(2*(n-i)-1)+[str(i%10)]+[" "]*(i-1)) for i in range(1,n)]+[(lambda r: r+"".join([r[1:] for j in range(1,x)]) )(" "*(n-1)+str(n%10)+" "*(n-1))]+[(lambda r: "".join(r)+"".join(["".join(r[1:]) for j in range(1,x)]))([" "]*(i-1)+[str(i%10)]+[" "]*(2*(n-i)-1)+[str(i%10)]+[" "]*(i-1)) for i in range(n-1,0,-1)])) if n>0 else ""

#this one-liner was not so easy :D Dedicated to my fellow codewarrior ChristianECooper:
#knowing that my code can be read by someone that good and precise keeps me surely
#motivated; against him I may have the upper hand just with regexes (and he
#certainly is better at explaining), but I won't give up that easily ;)

