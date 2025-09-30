rows, cols = map(int, input("Enter rows and columns: ").split())

# Get matrix
matrix = []
print(f"Enter {rows} rows:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix entered:")
for row in matrix:
    print(*row)

#print("Digonals:")
#dig = []
#for i in range(rows):
 #   if 