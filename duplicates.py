from collections import Counter
f=0
n= int(input()) 
numbers = list(map(int, input().split())) 
freq=Counter(numbers)
for key in freq:
    if freq[key]>1:
        f=1
        break
if f==1:
    print("true")
else:
    print("false")
    

