import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)

#step1
b = a[:2, 1:3]
print(b)

b[0, 0] = 800

print(a)

#step2
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)


#step3
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)