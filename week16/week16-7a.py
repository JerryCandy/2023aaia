a=list(map(int,input().split() ))
a.sort()
ans =a[0]+a[1]*10+a[2]*100+1
print(ans,end='')