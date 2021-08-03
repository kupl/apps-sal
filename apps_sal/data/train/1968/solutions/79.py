class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''
        Build trie from the folders, whenever a folder ends, just drop all of its children (subfolders) in the trie.
        Time O(N) to build the trie and do DFS
        Space O(N) for the trie
        '''
        trie = {}
        for f in folder:
            path = f.split('/')[1:]
            cur = trie
            for idx, p in enumerate(path):
                if idx == len(path) - 1:
                    # this is the ending folder
                    cur[p] = '#'
                else:
                    if p in cur:
                        if cur[p] != '#':
                            cur = cur[p]
                        else:
                            # we see an ending folder, stop adding subfolders to it
                            break
                    else:
                        cur[p] = {}
                        cur = cur[p]

        # do a DFS of the trie to get the answers
        ans = []

        def dfs(cur_dir, path):
            if cur_dir == '#':
                ans.append('/' + '/'.join(path))
                return
            for k in cur_dir:
                dfs(cur_dir[k], path + [k])
            return
        dfs(trie, [])
        return ans
