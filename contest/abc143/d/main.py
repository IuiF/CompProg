n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ans += L[i] + L[j] > L[k]


print(ans)
