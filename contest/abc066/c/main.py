from collections import deque


n = int(input())
b = deque([])
a = list(map(int, input().split()))
for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])

b = list(b)

if n % 2 == 1:
    b = b[::-1]

print(*b)
