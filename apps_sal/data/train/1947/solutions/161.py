class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dictionary = dict()
        for i in range(len(B)):
            prev_dict = dict(dictionary)
            for j in range(len(B[i])):
                char = B[i][j]
                if char in dictionary:
                    dictionary[char] += 1
                else:
                    dictionary[char] = 1
                if char not in prev_dict:
                    prev_dict[char] = 0

            for key, value in list(prev_dict.items()):
                if dictionary[key] - prev_dict[key] > prev_dict[key]:
                    dictionary[key] -= prev_dict[key]
                else:
                    dictionary[key] = prev_dict[key]

        answer = []
        for i in range(len(A)):
            current_dict = dict(dictionary)
            for j in range(len(A[i])):
                char_a = A[i][j]
                if char_a in current_dict:
                    current_dict[char_a] -= 1

            include_word = True
            for key, value in list(current_dict.items()):
                if value > 0:
                    include_word = False

            if include_word:
                answer.append(A[i])

        return answer
