n=list(map(int,input().split()))
l=list(map(int,input().split()))
a=n[1]
m=0
sum1=0
for i in range(a):
    m=max(l)
    sum1+=m
    l.remove(m)
print(sum1)
