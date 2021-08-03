import string
from collections import defaultdict
import time
class Node:
    def __init__(self, char):
        self.char = char
        self.count = 0
        self.children = {}
    def add_word(self, word):
        current = self
        for char in word:
            current = current.children.setdefault(char, Node(char))
        current.count += 1
        
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = Node(None)
        for word in words:
            sorted_word = ''.join(sorted(set(word)))
            trie.add_word(sorted_word)
            
        def get_word_count(puzzle):
            first_char = puzzle[0]
            sorted_puzzle = ''.join(sorted(puzzle))
            count = 0
            def helper(i, node):
                if i == len(puzzle):
                    yield node
                    return
                char = sorted_puzzle[i]
                if char == first_char:
                    if char in node.children:
                        for yielded_node in helper(i+1, node.children[char]):
                            yield yielded_node
                else:
                    for yielded_node in helper(i+1, node):
                        yield yielded_node
                    if char in node.children:
                        for yielded_node in helper(i+1, node.children[char]):
                            yield yielded_node

            for yielded_node in helper(0, trie):
                count += yielded_node.count
            return count
        
        retval = [0] * len(puzzles)
        for i, puzzle in enumerate(puzzles):
            retval[i] = get_word_count(puzzle)
        
        return retval
            
        
\"\"\"
        puzzle_index_set_lookup = defaultdict(set)
        for i, puzzle in enumerate(puzzles):
            for char in puzzle:
                puzzle_index_set_lookup[char].add(i)
        
        cached_puzzle_index_list = {}
        def get_puzzle_index_list(sorted_word):
            puzzle_index_list = cached_puzzle_index_list.get(sorted_word[:4])
            if puzzle_index_list is not None:
                return puzzle_index_list
            for i, char in enumerate(sorted_word[:4]):
                if i == 0:
                    puzzle_index_list = list(puzzle_index_set_lookup[char])
                else:
                    next_puzzle_index_list = []
                    current_puzzle_index_set = puzzle_index_set_lookup[char]
                    for puzzle_index in puzzle_index_list:
                        if puzzle_index in current_puzzle_index_set:
                            next_puzzle_index_list.append(puzzle_index)
                    puzzle_index_list = next_puzzle_index_list
            cached_puzzle_index_list[sorted_word[:4]] = puzzle_index_list
            return puzzle_index_list
        
        retval = [0] * len(puzzles)
        puzzle_sets = [set(puzzle) for puzzle in puzzles]
        for word in words:
            sorted_word = ''.join(sorted(word))
            for puzzle_index in get_puzzle_index_list(sorted_word):
                puzzle_set = puzzle_sets[puzzle_index]
                if puzzles[puzzle_index][0] in word:
                    match = True
                    for char in word:
                        if char not in puzzle_set:
                            match = False
                            break
                    if match:
                        retval[puzzle_index] += 1
        return retval
\"\"\"
    
    
    
    
    
    
    
\"\"\"
    def get_filtered_words(self, words, puzzles):
        filtered_words = defaultdict(list)
        char_counts = defaultdict(int)
        for word in words:
            word_set = set(word)
            for char in word_set:
                char_counts[char] += 1
                filtered_words[char].append(word)
        return filtered_words, char_counts
                
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        print (time.time())
        filtered_words, char_counts = self.get_filtered_words(words, puzzles)
        #print (filtered_words, char_counts)
        print (time.time(), char_counts)
        print (len(words), [len(word_list) for word_list in filtered_words.values()])
        
        def get_max_missing_char(puzzle_set):
            max_missing_char = None
            max_missing_char_count = -1
            for char in string.ascii_lowercase:
                if char in puzzle_set:
                    continue
                # This is a missing char.. identify the one that occurs the most so we can filter it
                missing_char_count = char_counts[char]
                if missing_char_count > max_missing_char_count:
                    max_missing_char_count = missing_char_count
                    max_missing_char = char
            return max_missing_char
        
        double_filtered_words = defaultdict(lambda: defaultdict(list))
        for first_char, word_list in filtered_words.items():
            for word in word_list:
                word_set = set(word)
                for missing_char in string.ascii_lowercase:
                    if missing_char not in word_set:
                        double_filtered_words[first_char][missing_char].append(word)
        #print(double_filtered_words)
        print(time.time())
        for char, missing_char_dict in double_filtered_words.items():
            print(char, [len(word_list) for word_list in missing_char_dict.values()])
        return
        
        retval = []
        for puzzle in puzzles:
            puzzle_set = set(puzzle)
            count = 0
            #print (puzzle, get_max_missing_char(puzzle_set), double_filtered_words[puzzle[0]][get_max_missing_char(puzzle_set)])
            for word in double_filtered_words[puzzle[0]][get_max_missing_char(puzzle_set)]:
                match = True
                for char in word:
                    if char not in puzzle_set:
                        match = False
                        break
                if match:
                    count += 1
            retval.append(count)
        return retval
        
\"\"\"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
\"\"\"
        retval = []
        for puzzle in puzzles:
            puzzle_set = set(puzzle)
            first_char = puzzle[0]
            count = 0
            for word in words:
                found_first_char = False
                found_all_chars = True
                for char in word:
                    if char == first_char:
                        found_first_char = True
                    elif char not in puzzle_set:
                        found_all_chars = False
                        break
                if found_first_char and found_all_chars:
                    count += 1
            retval.append(count)
        return retval
\"\"\"
