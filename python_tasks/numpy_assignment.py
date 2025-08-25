import numpy as np

print("Part 1 : ")
print("EX.1 : ")
print("a) ")
arr = np.arange(0, 21, 2)
print(arr)

print()
print("b) ")
matrix3x3 = np.identity(3)
print(matrix3x3)

print()
print("C) ")
ones_arr4x4 = np.ones((4, 4))
print(ones_arr4x4)

print()
print("d) ")
arr_spaced = np.linspace(5, 50, 10)
print(arr_spaced)

print()
print("EX.2&3 : ")
print("a) ")
conv_arr = np.array([10, 20, 30, 40, 50])
print(conv_arr)
print(f"shape = {conv_arr.shape} size = {conv_arr.size} type : {type(conv_arr)}")

print()
print("b.1) ")
matrix3x3_rand = np.random.rand(3, 3)
print(matrix3x3_rand)
print(
    f"shape = {matrix3x3_rand.shape} size = {matrix3x3_rand.size} type : {type(matrix3x3_rand)}"
)


print()
print("b.2) ")
matrix3x3_randn = np.random.randn(3, 3)
print(matrix3x3_randn)
print(
    f"shape = {matrix3x3_randn.shape} size = {matrix3x3_randn.size} type : {type(matrix3x3_randn)}"
)


print()
print("b.3) ")
matrix3x3_randint = np.random.randint(0, 10, (3, 3))
print(matrix3x3_randint)
print(
    f"shape = {matrix3x3_randint.shape} size = {matrix3x3_randint.size} type : {type(matrix3x3_randint)}"
)

print()
print(
    "====================================================================================="
)
print()

print("Part 2 : ")
print("EX.1 : ")
print("a) ")

sel_arr = np.array([5, 10, 15, 20, 25, 30])
first = sel_arr[0]
print(f"The first element = {first}")
print("b) ")
last3 = sel_arr[-3:]
print(f"The last three elements = {last3}")
print("c) ")
elem1to4 = sel_arr[1:5]
print(f"The elements at index positions 1 to 4 = {elem1to4}")

print()
print("EX.2 : ")

matr3x3 = np.arange(1, 10).reshape(3, 3)
print(matr3x3)
print("a) ")
sec_row = matr3x3[1]
print(f"Select the second row = {sec_row}")

print("b) ")
first_tow_col = matr3x3[:, 0:2]
print(f"Select the first two columns = \n{first_tow_col}")

print("c) ")
sub2x2 = matr3x3[0:2, 0:2]
print(f"Extract a sub-matrix of shape (2,2) = \n{sub2x2}")

print()
print("EX.3 : ")
mat3x3 = np.random.randint(0, 10, (3, 3))
print(mat3x3)
print("a)")
mat3x3 += 10
print(f"Create a 3x3 matrix and add 10 to every element = \n{mat3x3}")

print()
print("b)")
mat3x3[:, 0:2] *= 2
print(f"Multiply the first column by 2 = \n{mat3x3}")

print()
print("EX.4 : ")
num_arr = np.arange(0, 10)
print(num_arr)
num = num_arr[0:6]
num[0:6] = 9
print(f"shallow : {num}")
print(f"original array : {num_arr}")

print()

num_arr1 = np.arange(0, 10)
print(num_arr1)
num_copy = num_arr1[0:6].copy()
num_copy[0:6] = 6
print(f"Copy : {num_copy}")
print(f"original array : {num_arr1}")

print()
print("EX.5 : ")
arr_fancy = np.arange(10, 101, 10)
print(arr_fancy)
select_ele = arr_fancy[[0, 3, 5]]

print(select_ele)
print()
print(
    "====================================================================================="
)
print()

print("Part 3 : ")
print("EX.1 : ")

arr_op = np.array([3, 7, 2, 9, 12, 5, 10])
print(arr_op)
print(f"maximum = {arr_op.max()}")
print(f"minumum = {arr_op.min()}")
print(f"index of min = {arr_op.argmin()}")


print()
print("EX.2 : ")
arr_arith = np.array([1, 2, 3, 4, 5])
print(arr_arith)

print("a)")
print(np.sqrt(arr_arith))

print()
print("b)")
print(np.exp(arr_arith))

print()
print("c)")
print(np.sin(arr_arith))

print()
print("d)")
print(np.log(arr_arith))
