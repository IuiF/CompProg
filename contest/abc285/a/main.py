ls = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6, 7],
    [2, 8, 9],
    [2, 10, 11],
    [3, 12, 13],
    [3, 14, 15],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
a, b = map(int, input().split())
if b in ls[a]:
    print("Yes")
else:
    print("No")
