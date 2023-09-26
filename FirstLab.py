import numpy as np


def ref(matrix):
    rows, cols = matrix.shape

    arr = []

    current_row = 0

    for current_col in range(cols):

        pivot_row = None
        for i in range(current_row, rows):
            if matrix[i, current_col] == 1:
                pivot_row = i
                break
        arr.append(pivot_row)
        if pivot_row is not None:
            matrix[current_row], matrix[pivot_row] = matrix[pivot_row], matrix[current_row]

            for i in range(current_row + 1, rows):
                if matrix[i, current_col] == 1:
                    matrix[i] = (matrix[i] + matrix[current_row]) % 2

            current_row += 1
    return matrix, arr


def rref(matrix):
    ref_matrix, points_row = ref(matrix)
    for col in range(len(points_row)):
        if points_row[col] is not None:
            for i in range(points_row[col] - 1, -1, -1):
                if ref_matrix[i][col] == 1:
                    ref_matrix[i] = (ref_matrix[points_row[col]] + ref_matrix[i]) % 2
    return ref_matrix


def shape_mat(matrix):
    non_zero_rows = [i for i, row in enumerate(matrix) if any(row != 0)]
    return matrix[non_zero_rows]


def delete_col(matrix, lead):
    matrix = np.delete(matrix, lead, axis=1)
    return matrix


def insert_row(matrix, lead):
    i_mat = np.eye(6,dtype=int)
    h = np.zeros((matrix.shape[0] + i_mat.shape[0], matrix.shape[1]), dtype=int)
    x_counter = 0
    i_counter = 0
    for i in range(matrix.shape[0] + i_mat.shape[0]):
        if i in lead:
            h[i] = matrix[x_counter]
            x_counter += 1
        else:
            h[i] = i_mat[i_counter]
            i_counter += 1
    return h


matrix = np.array([[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                   [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                   [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                   [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]])

ref_matrix, arr = ref(matrix.copy())
print("Матрица в ступенчатом виде:")
print(ref_matrix, '\n')

rref_matrix = rref(ref_matrix.copy())
print("Матрица в приведённом виде:")
print(rref_matrix, '\n')

G_matrix = shape_mat(ref_matrix)
new_shape = shape_mat(rref_matrix)
row, col = new_shape.shape
print(new_shape, '\n', 'k =', row, '\n', 'n =', col)

lead = [arr.index(i) for i in arr if i is not None]
print(f'lead: {lead}')

x = delete_col(new_shape, lead)
print('x: \n', x)

i = np.eye(6, dtype=int)

H = insert_row(x, lead)

u = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0],                   #1.4.2 Взять все двоичные слова длины k, умножить каждое на G.
              [0, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0],
              [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 1],
              [0, 1, 1, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 0, 1, 0, 1],
              [1, 0, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 1, 0],
              [1, 1, 0, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]])
for i in range(len(u)):
    v = u[i]@G_matrix % 2
    print('v@H = ', v@H % 2, 'for u = ', u[i])

codewords = u@G_matrix % 2
#print(H)
#print(codewords)

def distance_calc(G, k, n):    #1.4 Вычислить кодовое расстояние получившегося кода.
    for i in range(k - 1):
        for j in range(i + 1, k):
            xor_rows = sum((G[i] + G[j]) % 2)
            if xor_rows < n:
                n = xor_rows
    return n, n - 1

print(f"d = {distance_calc(G_matrix, row, col)[0]}\nt = {distance_calc(G_matrix, row, col)[1]}")

