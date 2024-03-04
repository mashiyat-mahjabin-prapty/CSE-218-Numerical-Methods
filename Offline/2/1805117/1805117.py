import numpy as np

def GaussianElimination(M, N, d):
    size = len(M)
    for i in range(n-1):
        maximum = abs(M[i][i])
        maxrow = i
        for u in range(i, n):
            if abs(M[u][i]) > maximum:
                maximum = M[u][i]
                maxrow = u
        for v in range(n):
            temp = M[i][v]
            M[i][v] = M[maxrow][v]
            M[maxrow][v] = temp
        temp = N[i]
        N[i] = N[maxrow]
        N[maxrow] = temp
        for j in range(i + 1, n):
            ratio = M[j][i] / M[i][i]
            for k in range(n):
                M[j][k] = M[j][k] - ratio * M[i][k]
            N[j] = N[j] - N[i] * ratio
            if d:
                print('Step ', i+1)
                print(M)
                D = np.array([N]).T
                print(D)
                print()
    ans = [[0] for i in range(n)]
    ans[n-1] = N[n-1]/M[n-1][n-1]    
    for p in range(n-2, -1, -1):
        ans[p] = N[p]
        for q in range(p+1, n):
            ans[p] = ans[p] - M[p][q]*ans[q]
        ans[p] = ans[p]/M[p][p]
    return ans

        
n = int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    a[i] = list(map(float, input().split()))

A = np.array(a)

print(A)

b = [[0] for i in range(n)]

for i in range(n):
    b[i] = float(input())

B = np.array(b)
print(np.array([B]).T)
print()

pivot = np.array(GaussianElimination(A, B, d=True))
for index in pivot:
    print ("{0:0.4f}".format(index))
