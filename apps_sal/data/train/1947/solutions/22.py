from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universal_words = []
        required_counts = {}
        for pattern in B:
            for char in pattern:
                char_sum = sum(1 for i in pattern if i == char)
                if char not in required_counts or required_counts[char] < char_sum:
                    required_counts[char] = char_sum
        print(required_counts)
        for word in A:
            universal = True
            for char in required_counts:
                char_count = sum(1 for i in word if i == char)
                if char_count < required_counts[char]:
                    universal = False
            if universal:
                universal_words.append(word)
        return universal_words
