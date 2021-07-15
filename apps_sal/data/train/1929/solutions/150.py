class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Node(\"\", None)
        for word in words:
            prev = self.root
            substr = \"\"
            for letter in word:
                substr += letter
                is_final = len(substr) == len(word)
                if letter not in prev.children:
                    prev.children[letter] = Node(substr, prev)
                
                curr = prev.children[letter]
                if is_final:
                    curr.is_final = True

                prev = curr

        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.word:
                letter = curr.word[-1]

                parent_suffix = curr.parent.suffix
                while parent_suffix:
                    if letter in parent_suffix.children:
                        curr.suffix = parent_suffix.children[letter]
                        break
                    else:
                        parent_suffix = parent_suffix.suffix
                if curr.suffix is None:
                    curr.suffix = self.root
                
                suffix = curr.suffix
                while suffix:
                    if suffix.is_final:
                        curr.dictionay_suffix = suffix
                    suffix = suffix.suffix

            for _, child in curr.children.items():
                queue.append(child)

        self.curr = self.root

    def query(self, letter: str) -> bool:
        # print(f\"Input: {letter}\")
        while letter not in self.curr.children:
            if self.curr.suffix:
                self.curr = self.curr.suffix
            else:
                return False
        self.curr = self.curr.children[letter]
        # print(f\"\\tcurr={self.curr.word}\")

        return self.curr.is_final or (self.curr.dictionay_suffix is not None)

    def query_all(self, letters: str) -> List[bool]:
        # self.print_all()
        result = []
        for letter in letters:
            result.append(self.query(letter))
        return result

    def print_all(self):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            curr.print()
            for _, child in curr.children.items():
                queue.append(child)


class Node:
    def __init__(self, word, parent):
        self.word = word
        self.parent = parent

        self.is_final = False
        self.children = {}
        self.suffix = None
        self.dictionay_suffix = None

    def print(self):
        final_str = \"*\" if self.is_final else \"\"
        print(f\"({self.word}) {final_str}\")
        for letter, child in self.children.items():
            print(f\"\\t{letter} -> ({child.word})\")
        if self.parent:
            print(f\"\\t[parent] -> ({self.parent.word})\")
        if self.suffix:
            print(f\"\\t[suffix] -> ({self.suffix.word})\")
        dict_suffix_str = f\"({self.dictionay_suffix.word})\" if self.dictionay_suffix else \"None\"
        print(f\"\\t[dict_suffix] -> {dict_suffix_str}\")
        print()

