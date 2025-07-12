n=int(input())
row = list(map(int, input().split()))
hm=0
for i in range(n):
    for j in range(i+1,n):
        if i!=n-1:
            maxi=row[j]-row[i]
            hm=max(maxi,hm)
print(hm)
