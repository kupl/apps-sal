class Matrix:
    def __init__(self, data):
        self._data = data
        self._rows = len(data)
        self._columns = len(data[0])


    @classmethod
    def empty(cls, rows, columns):
        data = [[None for _ in range(columns)] for _ in range(rows)]

        return cls(data)


    def __getitem__(self, key):
        return self._data[key]
        
      
    @property
    def data(self):
        return self._data


    @property
    def rows(self):
        return self._rows


    @property
    def columns(self):
        return self._columns


    def row(self, row_index):
        for elem in self._data[row_index]:
            yield elem


    def column(self, column_index):
        for row in self._data:
            yield row[column_index]


    def __str__(self):
        str_rows = []
        for row in self._data:
            str_rows.append('  '.join(map(str, row)))

        return "\n".join(str_rows)


    def __mul__(self, matrix):
        result = Matrix.empty(self.rows, self.columns)

        for result_row in range(result.rows):
            for result_column in range(result.columns):
                current_row = self.row(result_row)
                current_column = matrix.column(result_column)

                result_element = 0
                while True:
                    try:
                        row_element = next(current_row)
                        column_element = next(current_column)
                    except StopIteration:
                        break
                    result_element += row_element * column_element

                result[result_row][result_column] = result_element

        return result


def matrix_mult(a, b):
  product = Matrix(a) * Matrix(b)
  return product.data
  
  
  

