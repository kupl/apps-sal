build_trie = lambda *words: (cheker(words) or {})
    
cheker = lambda wos, i=1: None if not wos else {l: cheker(tuple(x for x in wos if x[:i]==l and x!=l), i+1) for l in set(e[:i] for e in wos if e)}

