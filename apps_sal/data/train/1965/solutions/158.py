class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a,b,c=[[] for _ in range(n+1)],[[] for _ in range(n+1)],[[] for _ in range(n+1)]
        for k,i,j in edges:
            if k==1:
                a[i].append(j)
                a[j].append(i)
            elif k==2:
                b[i].append(j)
                b[j].append(i)
            else:
                c[i].append(j)
                c[j].append(i)
        d,st=[1]*(n+1),[1]
        d[0],d[1]=0,0
        while st:
            i=st.pop()
            for j in a[i]:
                if d[j]:
                    d[j]=0
                    st.append(j)
            for j in c[i]:
                if d[j]:
                    d[j]=0
                    st.append(j)
        if any(x for x in d): return -1
        d,st=[1]*(n+1),[1]
        d[0],d[1]=0,0
        while st:
            i=st.pop()
            for j in b[i]:
                if d[j]:
                    d[j]=0
                    st.append(j)
            for j in c[i]:
                if d[j]:
                    d[j]=0
                    st.append(j)
        if any(x for x in d): return -1
        d,s=[1]*(n+1),0
        for i in range(1,n+1):
            if d[i]:
                st,d[i]=[i],0
                while st:
                    i=st.pop()
                    for j in c[i]:
                        if d[j]:
                            d[j],s=0,s+1
                            st.append(j)
        return len(edges)-(2*n-2-s)
