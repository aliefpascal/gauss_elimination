# n = int(input("Please input number of unknowns and equations: "))
# A = []
#
# # Prompt user to input the elements of the augmented matrix
# for i in range(n):
#     row = []
#     for j in range(n+1):
#         element = float(input(f"Please input a_{i+1}{j+1}: "))
#         row.append(element) #elemet dimasukin ke row pake fungsi append()
#     A.append(row)
#
# print("Augmented matrix A:")
# for row in A:
#     print(row)
#


# Input number of unknowns and equations
n = int(input("Please input number of unknowns and equations: "))

# Initialize augmented matrix A
A = []
for i in range(n):
    row = []
    for j in range(n+1):
        element = float(input(f"Please input a_{i+1}{j+1}: "))
        row.append(element)
    A.append(row)

# Elimination process
for i in range(n-1):
    # Find p
    p = i
    while p < n and A[p][i] == 0:
        p += 1
    if p == n:
        print("No unique solution exists")
        break
    # Swap rows if necessary
    if p != i:
        A[i], A[p] = A[p], A[i]
    # Perform elimination
    for j in range(i+1, n):
        m = A[j][i] / A[i][i]
        for k in range(i, n+1):
            A[j][k] -= m * A[i][k]

# Check for unique solution
if A[n-1][n-1] == 0:
    print("No unique solution exists")
else:
    # Backward substitution
    x = [0] * n
    x[n-1] = A[n-1][n] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        s = A[i][n]
        for j in range(i+1, n):
            s -= A[i][j] * x[j]
        x[i] = s / A[i][i]
    # Output solution
    print("Solution:", x)
