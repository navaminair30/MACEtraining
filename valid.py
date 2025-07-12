r=input()
p=0
valid=True 

for c in r:
    if c=='{':
        p+=1
    elif c=='}':
        p-=1
    if p<0:
        valid=False
        break
        
        
if p==0 and valid:
    print("Matching")
else:
    print("Not Matching")
