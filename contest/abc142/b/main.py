n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i >= k:
        ans += 1
print(ans)
