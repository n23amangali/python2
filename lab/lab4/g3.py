def generator(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for j in generator(n):
    print(j,end=' ')