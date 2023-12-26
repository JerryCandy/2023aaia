a= int(input())

ten=1
while a>0:
	now=a%10*ten
	print(now,end=' ')
	a=a//10
	ten = ten*10