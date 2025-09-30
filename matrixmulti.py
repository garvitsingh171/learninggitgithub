rows, cols = map(int,input('Enter the number of rows and coloumns: ').split())

mat1 = []
mat2 = []

print("Enter rows for Mat1")
for i in range(rows):
    row = list(map(int,input(f'Enter {i} row: ').split()))
    mat1.append(row)

print('Enter rows for Mat2')
for j in range(rows):
    row = list(map(int,input(f'Enter {i} row: ').split()))
    mat2.append(row)

print(mat1)
print(mat2)

mat3 = []
for i in range(rows):
    rowd = []
    for j in range(cols):
        num = 0
        for k in range(rows):
            num += (mat1[i][k])*(mat2[k][j])
        rowd.append(num)
    mat3.append(rowd)
print(mat3)