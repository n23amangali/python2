def square(a,b):
    for i in range(a,b):

        yield i*i
a=int(input())
b=int(input())
for j in square(a,b):
    print(j,end=' ')