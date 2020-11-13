
def first(n,it):
    for i in range(n):
        yield it[i]

n=20
f=first(100, [2,4,5,7,2])
d=first(20,range(50, 200))

for i in range(n):
    print(next(d))

for i in range(n):
    print(next(f))