#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
for row in new_matrix:
    squared_row = []
    for element in row:
        squared_element = element ** 2

    squared_row.append(squared_element)
    new_matrix.append(squared_row)
return new_matrix
