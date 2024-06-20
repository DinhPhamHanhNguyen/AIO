source = input("First word: ")
target = input("Second word: ")

M = len(source) + 1
N = len(target) + 1


matrix = [[0] * (N) for _ in range(M)]

for i in range(N):
    matrix[0][i] = i

for i in range(M):
    matrix[i][0] = i

for i in range(1, M):
    for k in range(1, N):
        del_cost = matrix[i - 1][k] + 1
        ins_cost = matrix[i][k - 1] + 1
        sub_cost = matrix[i - 1][k - 1] + \
            (0 if source[i - 1] == target[k - 1] else 1)
        matrix[i][k] = min(del_cost, ins_cost, sub_cost)

print(matrix[M-1][N-1])
