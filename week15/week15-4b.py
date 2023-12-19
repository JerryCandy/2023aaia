a= int(input())

ans=0
for i in range(1,1001):
	if a == i*i:
		ans=i
		
print(ans,end='')