def trace_of_matrix_v2(matrix):
 _list = []
 for diff in range(len(matrix)):
  sum1, sum2, index = (0, 0, diff)
  for i in range(len(matrix) - diff):
   sum1 += matrix[index][i]
   sum2 += matrix[i][index]
   index += 1
  _list.append(sum1)
  _list.append(sum2)
 return max(_list)


def __starting_point():
 t = int(input())
 for _ in range(t):
  n = int(input())
  _list = []
  for _ in range(n):
   _list.append(list(map(int, input().split())))
  print(trace_of_matrix_v2(_list))
__starting_point()
