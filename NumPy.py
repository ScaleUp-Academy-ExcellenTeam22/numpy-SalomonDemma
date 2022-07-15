import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch


if __name__ == "__main__":

    print("""
            +--------------+
            |  Question 1  |
            +--------------+
            """)

    range_vector = np.arange(21, dtype='int')
    range_vector[(range_vector >= 9) & (range_vector <= 15)] *= (-1)
    print(range_vector)

    print("""
            +--------------+
            |  Question 3  |
            +--------------+
            """)

    matrix = np.arange(1, 13).reshape((3, 4))
    print('The Matrix:\n', matrix)
    print('The Dimension:\n', matrix.shape)

    print("""
            +--------------+
            |  Question 5  |
            +--------------+
            """)

    original_matrix = np.arange(1, 13).reshape((3, 4))
    new_vector = np.array([1, 2, 3, 4])
    print('Original matrix:\n', original_matrix)
    print('New Vector\n', new_vector)

    result = np.empty_like(original_matrix)
    for row in range(original_matrix.shape[0]):
        result[row, :] = original_matrix[row, :] + new_vector

    print('Result:\n', result)

    print("""
            +--------------+
            |  Question 7  |
            +--------------+
            """)

    random_array = np.random.random((4, 4))
    print("Random 4x4 array:")
    print(random_array)
    print("Result 4x4 array:")
    random_array[[0, -1], :] = random_array[[-1, 0], :]
    print(random_array)

    print("""
            +--------------+
            |  Question 9  |
            +--------------+
            """)

    array1 = np.arange(1, 10).reshape((3, 3))
    array2 = np.arange(11, 20).reshape((3, 3))

    print("Array1:")
    print(array1)
    print("Array2:")
    print(array2)
    print("Result:")
    print(np.multiply(array1, array2))

    print("""
            +---------------+
            |  Question 11  |
            +---------------+
            """)

    print("Result:")
    print(np.eye(3))

    print("""
            +--------------+
            |  Question 13 |
            +--------------+
            """)

    array1 = np.arange(10, 40, 10)
    array2 = np.arange(40, 70, 10)

    print("Array1:")
    print(array1)
    print("Array2:")
    print(array2)
    print("Result:")
    print(np.dstack((array1, array2)))

    print("""
            +--------------+
            |  Question 15 |
            +--------------+
            """)

    three_d_array = np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)
    print(three_d_array)

    print("""
            +--------------+
            |  Question 17 |
            +--------------+
            """)

    array = np.arange(12).reshape((2, 6))
    print("Original array:")
    print(array)
    median = np.median(array)
    print("Median of said array:\n", )
    print(median)

    print("""
            +--------------+
            |  Question 19 |
            +--------------+
            """)

    a = patch.Rectangle((1, 0), width=3, height=6, facecolor='blue', edgecolor='grey')
    b = patch.Rectangle((4, 0), width=3, height=6, facecolor='white', edgecolor='grey')
    c = patch.Rectangle((7, 0), width=3, height=6, facecolor='red', edgecolor='grey')
    fig, ax = py.subplots()
    ax.add_patch(a)
    ax.add_patch(b)
    ax.add_patch(c)

    py.axis('equal')
    py.show()

