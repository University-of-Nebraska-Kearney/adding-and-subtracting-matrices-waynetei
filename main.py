def get_matrix():
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            value = int(input("Value at ({r+1},{c+1}): "))
            row.append(value)
        matrix.append(row)

    return matrix


def add_matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices cannot be added (different sizes).")
        return None

    result = []
    for r in range(len(matrix1)):
        row = []
        for c in range(len(matrix1[0])):
            row.append(matrix1[r][c] + matrix2[r][c])
        result.append(row)

    return result


m1 = get_matrix()
m2 = get_matrix()

sum_matrix = add_matrix(m1, m2)

if sum_matrix is not None:
    print("Sum:", sum_matrix)

if __name__ == "__main__":
    main()