class Solution:
    def wordSubsets(self, A, B):
        '''
        :type A: list of str
        :type B: list of str
        :rtype: list of str
        '''
        b_count = [0] * 26

        # Collecting the constraints into a character mapping
        for word in B:
            tmp_count = self.count(word)

            for i in range(0, 26):
                b_count[i] = max(b_count[i], tmp_count[i])

        # Testing each character in A
        output = []
        for word in A:
            tmp_count = self.count(word)

            universal = True
            for i in range(0, 26):
                if tmp_count[i] < b_count[i]:
                    universal = False

            if universal:
                output.append(word)

        return output

    def count(self, word):
        output = [0] * 26

        for letter in word:
            idx = ord(letter) - ord(\"a\")
            output[idx] += 1

        return output


