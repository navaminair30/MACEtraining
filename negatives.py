r=int(input())
d=int(input())
m=[]
for i in range(r):
    row = list(map(int, input().split()))
    m.append(row)
for row in m:
    row.sort()
count=0
for row in m:
    for c in row:
        if c<0:
            count+=1
print(count)
        
