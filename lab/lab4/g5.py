def generator(n):

    while n>=0:
        yield n
        n=n-1


n=int(input())

for j in generator(n):
    print(j,end=' ')