class Solution1:
    #1.Sort the folders;
    #2. For each folder check if the followings are child folders; if yes, ignore; otherwise, count it in
    \"\"\"
    I think the time complexity for method 2 is actually O(n * m * logn).
    Because the sort is based on merge sort for Object and time complexity of merge sort is O(n * logn). That means n * logn times comparing happened.
    For this question, it just makes the comparing time be O(m). Thus it won't increase the number of \"layers\" of merge sort to log(n * m).

    Time: O(n * m * log(n)), space: O(1)(excluding space cost of sorting part), where n = folder.length, m = average size of the strings in folder.

    \"\"\"
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        folder.sort()
        for f in folder:
            if not ans or not f.startswith(ans[-1] + '/'): #need '/' to ensure a parent.
                ans.append(f)
        return ans
    
    
class Trie:
    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.index = -1

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()
        for i in range(len(folder)):
            cur = self.root
            for c in folder[i]:
                cur = cur.sub[c]
            cur.index = i
        return self.bfs(self.root, folder)
    def bfs(self, trie: Trie, folder: List[str]) -> List[str]:
        q, ans = [trie], []
        for t in q:
            if t.index >= 0:
                ans.append(folder[t.index])
            for c in t.sub.keys():
                if '/' != c or t.index < 0:
                    q.append(t.sub.get(c))
        return ans
