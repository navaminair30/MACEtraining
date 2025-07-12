r, c = map(int, input().split())

m=[]
n=[]
s=[]
      
for i in range(r):
    row = list(map(int, input().split()))
    m.append(row)
print("First Matrix:")
for row in m:
    print(*row)
for i in range(r):
    row = list(map(int, input().split()))
    n.append(row)
print("Second Matrix:")
for row in n:
    print(*row)
for i in range(r):
    row = []
    for j in range(c):
        row.append(m[i][j] + n[i][j])
    s.append(row)

print("Sum of the two matrices is:")
for row in s:
    print(*row)
