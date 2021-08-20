class Solution:

    def __init__(self):
        self.result = []
        self.visited = None

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.visited = [0 for i in range(n)]
        self.__solve_n_queues(n, 0, [])
        return self.result

    @staticmethod
    def __not_diagonal(x, y, curr_answer):
        for (c_x, c_y) in enumerate(curr_answer):
            if abs(c_x - x) == abs(c_y - y):
                return False
        return True

    @staticmethod
    def visualize(curr_answer, n):
        answer = []
        for pos in curr_answer:
            answer.append('.' * pos + 'Q' + '.' * (n - pos - 1))
        return answer

    def __solve_n_queues(self, n, level, curr_answer):
        if level == n:
            self.result.append(Solution.visualize(curr_answer, n))
            return
        for i in range(n):
            if not self.visited[i] and Solution.__not_diagonal(level, i, curr_answer):
                self.visited[i] = 1
                curr_answer.append(i)
                self.__solve_n_queues(n, level + 1, curr_answer)
                curr_answer.pop()
                self.visited[i] = 0
