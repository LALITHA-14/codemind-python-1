marks = [[16, 19, 41, 32, 91],
         [45, 94, 42, 36, 11],
         [67, 81, 36, 42, 1],
         [9, 7, 17, 41, 47],
         [91, 94, 32, 16, 11]]
# create a new list called stats
# [[16, 91, 199], [11, 94, 228], [1, 81, 227], [7, 47, 121], [11, 91, 244]]
stats =[[min(i),max(i),sum(i)] for i in marks]
print(stats)
