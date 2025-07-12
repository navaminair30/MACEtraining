n=int(input(""))
day=list(map(int,input().split()))
night=list(map(int,input().split()))
limit=int(input())
extra=0
for i in range(n):
    sum=min(day)+max(night)
    if sum>limit:
        diff=sum-limit
        extra+=diff
    day.remove(min(day))
    night.remove(max(night))
print(extra*100)
