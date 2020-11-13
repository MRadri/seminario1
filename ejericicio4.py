def take_while(cond,it):
    i=0
    while cond(it[i]):
            yield(it[i])
            i+=1

d=take_while(lambda n: n<100, range(50, 200))
f=take_while(lambda n: n%2 == 0, [2,4,5,7,2])
for i in range(50,200):
   print(next(d))

for i in range(6):
    print(next(f))