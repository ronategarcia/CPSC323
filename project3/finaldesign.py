l = []
for i in range(1,4):
  for j in range(4, 0, -1):
    if i != j:
      l.insert(len(l),(i, j))

print(l)
l = [(i, j) for i in range(1, 4) for j in range(4, 0, -1) if i != j]
print(l)