import sys

sys.setrecursionlimit(10**6)
x = int(input())
n = 0
i = 1
while n < x:
    n += i
    i += 1

print(i - 1)
