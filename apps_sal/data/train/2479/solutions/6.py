class Solution:

    def judgeCircle(self, moves):
        m_list = list(moves)
        return m_list.count('U') == m_list.count('D') and m_list.count('R') == m_list.count('L')
