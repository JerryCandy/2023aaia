c=input()
if c>='A' and c<='Z': ans = 'U'
elif c>='a' and c<='z': ans = 'L'
elif c>='0' and c<='9': ans = 'D'
else: ans='O'
print(ans,end='')