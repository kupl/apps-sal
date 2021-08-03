class Solution:
    def findCircleNum(self, M):
        N = len(M)
        students = set()
        for i in range(N):
            students.add(i)

        num_grp = 0
        while students:
            num_grp += 1
            stack = [students.pop()]
            while stack and students:
                student = stack.pop()
                for i in range(N):
                    if M[student][i] == 1 and i in students:
                        stack.append(i)
                        students.discard(i)
        return num_grp
