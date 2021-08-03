class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B) or set(A) != set(B):
            return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)
                if counter > 2:
                    return False
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]
