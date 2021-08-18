class StreamChecker:

    def __init__(self, words: List[str]):
        trie = {}

        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                    node = node[c]
                    node['fail'] = trie
                else:
                    node = node[c]

            node['end'] = True

        que = [trie[x] for x in trie]
        for node in que:
            for x in node:
                if x not in ('end', 'fail'):
                    p = node['fail']
                    while p != trie and x not in p:
                        p = p['fail']
                    if x in p:
                        node[x]['fail'] = p[x]
                        if 'end' in p[x]:
                            node[x]['end'] = True
                    que.append(node[x])
        self.trie = trie
        self.node = trie

    def query(self, x: str) -> bool:
        trie = self.trie
        node = self.node
        while node != trie and x not in node:
            node = node['fail']
        if x in node:
            node = node[x]
        self.node = node
        return 'end' in node
