s = list(input())
ans = [0, 0, 0, 0, 0, 0]
for i in s:
    ans[ord(i) - ord("A")] += 1
print(*ans)
