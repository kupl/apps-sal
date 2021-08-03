class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        counter = 0

        rows = len(mat)

        if rows > 0:
            columns = len(mat[0])

            for i in range(rows):
                for j in range(columns):

                    max_width = 0
                    max_height = 0

                    if mat[i][j] == 1:
                        counter += 1
                        max_width += 1
                        max_height += 1

                        for k in range(j + 1, columns):
                            if mat[i][k] == 1:
                                counter += 1
                                max_width += 1
                            else:
                                break

                        for l in range(i + 1, rows):
                            if mat[l][j] == 1:
                                counter += 1
                                max_height += 1
                                m_w = 1

                                for m in range(j + 1, columns):
                                    if mat[l][m] == 1 and m_w < max_width:
                                        counter += 1
                                        m_w += 1
                                    else:
                                        max_width = min(max_width, m_w)
                                        break
                            else:
                                break
                    else:
                        continue

        return counter
