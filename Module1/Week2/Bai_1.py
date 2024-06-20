num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
out = []
for i in range(len(num_list)-k+1):
    out.append(max(num_list[i: i+k]))

print(out)
