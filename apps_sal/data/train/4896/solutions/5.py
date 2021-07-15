 
def build_trie(*words):
    trie={} 
    k=''
    def recurse(trie,wd,k):
        for l in wd:
            k=k+l
            if k in trie:
                if trie[k]==None and len(wd)>1:
                  trie[k]={}
                recurse(trie[k],wd[1:],k)
            else:
                trie[k]={} if len(wd)>1 else None
                recurse(trie[k],wd[1:],k)
            return trie
    
    [recurse(trie,word,'') for word in words]
     
    return trie





 


