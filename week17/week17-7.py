a= list(map(int,input().split() ))
fast= min(a)
for i in range(len(a)):
	if a[i]==fast:
		ansI=i+1
		break

print(ansI,int(1.2*60*60/fast) )