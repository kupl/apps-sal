div=lambda n:[[i,n//i] for i in range(2,int(n**.5)+1) if not n%i]
def prod_int_part(n):
        li,parts = div(n),set()
        def recur(li, s=[]):
            parts.add(tuple(sorted(s)))
            for i in li:
                recur(div(i[1]),s+i if not s else s[:-1]+i)
        recur(li)
        return [len(parts)-1,list(max(parts,key=len))]
