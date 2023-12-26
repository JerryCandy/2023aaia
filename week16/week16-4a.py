N =int(input())
ans=0

for i in range(1,N+1):
	if i%2==1:ans+=i

print(ans, end='')