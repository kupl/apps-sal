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

    '''
    def __init__(self, words: List[str]):
        self.trie = defaultdict(tree)
        for word in words:
            node = self.trie
            for char in word:
                node = node[char]
            node['*'] = 1
        self.pointers_stack = []
        

    def query(self, letter: str) -> bool:
        answer = False
        if self.pointers_stack != []:
            index = 0
            while index < len(self.pointers_stack) and self.pointers_stack != []:
                root = self.pointers_stack[index]
                if letter in root.keys():
                    self.pointers_stack[index] = root[letter]
                    if root[letter]['*'] == 1:
                        answer = True
                    index += 1
                else:
                    self.pointers_stack.pop(index)
        if letter in self.trie.keys():
            root = self.trie[letter]
            self.pointers_stack.append(root)
            if root['*'] == 1:
                answer = True
        return answer
        
    '''
