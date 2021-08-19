from collections import defaultdict


def tree():
    return defaultdict(tree)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = defaultdict(tree)
        for word in words:
            node = self.trie
            for char in word[::-1]:
                node = node[char]
            node['*'] = 1
        self.current_list = []

    def query(self, letter: str) -> bool:
        match_found = True
        end_found = False
        self.current_list.insert(0, letter)
        i = 0
        node = self.trie
        while i < len(self.current_list):
            if self.current_list[i] in list(node.keys()):
                node = node[self.current_list[i]]
                if '*' in list(node.keys()):
                    end_found = True
                    break
            else:
                match_found = False
                break
            i += 1
        if '*' in list(node.keys()):
            end_found = True
        return end_found
    "\n    def __init__(self, words: List[str]):\n        # we store the words in a trie (nested defaultdictionary)\n        self.trie = defaultdict(tree)\n        for word in words:\n            node = self.trie\n            for char in word:\n                node = node[char]\n            node['*'] = 1\n        self.pointers_stack = []\n        # we keep a list of pointers which mark the beginnign of the words in the trie based on the queries in the trie and if we return True we just increment the last pointer in the pointers heirarchy to point to the new root down the hierarchy and if there is a new word that starts \n        # if we return False because we cannot find the current character in the current pointer we change the pointer to point to the beginning and if there is a word starting from that character we change it to it else we keep it null\n        # if we return False because we have not yet reached the end of the word however we have a corresponding character in the current pointer then we make a new entry to the pointers list which marks that this character may be because a new word has begun change the pointer to point to the latest character \n        \n    # def print_nested(self, d, indent=0):\n    #     for k, v in d.items():\n    #         print ('{}{!r}:'.format(indent * '  ', k))\n    #         self.print_nested(v, indent + 1)\n\n    def query(self, letter: str) -> bool:\n        # we keep on poping elements from the pointer stack as they mark the beginning of the words \n        # so our stack will be like [#q1q2q3, #q2q3, #q3] (actually it will be [#q3,#q3,#q3] and all q3 will be different nodes ) if we find the current character in q3 we increment the pointer in the last element and so now our stack becomes [#q1q2q3, #q2q3, #q3q4] -\n        # we keep on travelling the stack and if we do not find q4 somewhere we pop that node else we add q4 by incrementing the pointer till for all the elements in the stack\n        # eg there is no word starting with q2 and having q4 while there are some words having #q1q2q3q4 and #q3q4 format then our stack will look like [#q1q2q3q4, #q3q4] \n        # if for some value we find a word ending in q4 we return True else we return False\n        answer = False\n        if self.pointers_stack != []:\n            index = 0\n            while index < len(self.pointers_stack) and self.pointers_stack != []:\n                root = self.pointers_stack[index]\n                if letter in root.keys():\n                    self.pointers_stack[index] = root[letter]\n                    if root[letter]['*'] == 1:\n                        answer = True\n                    index += 1\n                else:\n                    self.pointers_stack.pop(index)\n        # finally we also need to add the current letter as a start of the word\n        if letter in self.trie.keys():\n            root = self.trie[letter]\n            self.pointers_stack.append(root)\n            if root['*'] == 1:\n                answer = True\n        return answer\n        \n    "
