"""
Go through matrix diagonal.
Matrix input from file.

"""

fp = open("input.txt")

row = list()
matrix = list()
for i in fp:
    row = i.split()
    row = [int(i) for i in row]
    matrix.append(row)

print("Upper Diagonal + middle diagonal")
#Diagonal Up
for diagonal in range(len(matrix)):
    for i in range(len(matrix)-diagonal):
        print(f"M[{i}][{i + diagonal}]: {matrix[i][i+diagonal]}")

print("Bottom Diagonal + middle diagonal")
#Diagonal Down
for diagonal in range(len(matrix)):
    for i in range(len(matrix)-diagonal):
        print(f"M[{i + diagonal}][{i}]: {matrix[i + diagonal][i]}")
