def generator(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input())
for even in generator(n):
    print(even,end=',')