def squares():
    i=1
    while True:
        yield i*i
        i=i+1


def first(n,it):
    for i in range(n):
        yield next(it)



def filter(cond,it):
    while True:
        aux=next(it)
        if cond(aux):
            yield aux


def take_while(cond,it):
    aux=next(it)
    while cond(aux):
            yield(aux)
            aux=next(it)

n=20
a=squares()
print("cuadrados")
prueba = first(100, squares())
for i in prueba:
    print(i)

print("TAKE WHILE")

prueba=take_while(lambda n: n<100, a)

for i in prueba:
    print(i)

#d=first(n,a)

print("FILTER")

f=filter(lambda n:  str(n) == str(n)[::-1],a)
for i in range(n):
    print(next(f))
