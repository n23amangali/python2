def generator(N):
    for i in range(N+1):
        yield i*i
N=int(input())
for square in generator(N):
    print(square,end=' ')