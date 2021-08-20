class Solution:

    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        A = [set(A[i]) for i in range(len(A))]
        answer = []
        for i in range(len(A)):
            answer.append(i)
            for j in range(len(A)):
                if i != j and len(A[i] | A[j]) == len(A[j]):
                    answer.pop()
                    break
        return answer
