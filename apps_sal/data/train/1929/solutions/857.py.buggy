# 题目要求按从旧到新顺序查询，因此可以将从旧到新的 query 存起来形成一个单词 stream。

# 比如：

# streamChecker.query(\"a\"); // stream： a
# streamChecker.query(\"b\"); // stream：ba
# streamChecker.query(\"c\"); // stream：cba
# 这里有两个小的点需要注意：

# 如果用数组来存储， 由于每次都往数组头部插入一个元素，因此每次 query 操作的时间复杂度为 $O(N)$，其中 $N$ 为截止当前执行 query 的次数，我们可以使用双端队列进行优化。
# 由于不必 query 形成的查询全部命中。比如 stream 为 cba 的时候，找到单词 c， bc， abc 都是可以的。如果是找到 c，cb，cba 比较好吧，现在是反的。其实我们可以反序插入是，类似的技巧在211.add-and-search-word-data-structure-design 也有用到。
# 之后我们用拼接的单词在 words 中查询即可， 最简单的方式当然是每次 query 都去扫描一次，这种方式毫无疑问会超时。

# 我们可以采用构建 Trie 的形式，即已空间环时间， 其代码和常规的 Trie 类似，只需要将 search(word) 函数做一个简单修改即可，我们不需要检查整个 word 是否存在， 而已 word 的前缀存在即可。

# 提示：可以通过对 words 去重，来用空间换区时间。

# 具体算法：

# init 中 构建 Trie 和 双端队列 stream
# query 时，往 stream 的左边 append 即可。
# 调用 Trie 的 search（和常规的 search 稍有不同， 我上面已经讲了）
# 核心代码（Python）：

# class StreamChecker:

#     def __init__(self, words: List[str]):
#         self.trie = Trie()
#         self.stream = deque([])

#         for word in set(words):
#             self.trie.insert(word[::-1])

#     def query(self, letter: str) -> bool:
#         self.stream.appendleft(letter)
#         return self.trie.search(self.stream)

# 关键点解析
# 前缀树模板
# 倒序插入




class Trie:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.Trie = {}

    def insert(self, word):
        \"\"\"
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        \"\"\"
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def search(self, word):
        \"\"\"
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        \"\"\"
        curr = self.Trie
        for w in word:
            if w not in curr:
                return False
            if \"#\" in curr[w]:
                return True
            curr = curr[w]
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = deque([])

        for word in set(words):
            self.trie.insert(word[::-1])   #反向插入

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.search(self.stream)

