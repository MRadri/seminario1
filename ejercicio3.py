def filter(cond,it):
    for i in range (len(it)):
        if cond(it[i]):
            yield(it[i])

d=filter(lambda n: n<100, range(50, 200))
f=filter(lambda n: n%2 == 0, [2,4,5,7,2])
for i in range(50,200):
    print(next(d))

for i in range(6):
    print(next(f))
