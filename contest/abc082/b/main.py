s = list(input())
s.sort()
s = "".join(s)

t = list(input())
t.sort(reverse=True)
t = "".join(t)


print("Yes" if s < t else "No")
