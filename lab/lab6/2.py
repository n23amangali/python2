a=input()
upper=0
lower=0
for i in range(len(a)):
    if a[i]>='a' and a[i]<='z':
        lower+=1
    else:
        upper+=1

print(upper,lower)