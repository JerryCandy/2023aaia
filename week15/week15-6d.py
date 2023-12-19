a,b=list(map(int,input().split() ))

if a>0 and b>0: ans=1
if a<0 and b>0: ans=2
if a<0 and b<0: ans=3
if a>0 and b<0: ans=4
print(ans)