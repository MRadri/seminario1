

def squares():
    i=1
    while True:
        yield i*i
        i=i+1

def filter(cond,it):
    while True:
        aux=next(it)
        if cond(aux):
            yield aux


def first(n,it):
    for i in range(n):
        yield next(it)

def take_while(cond,it):
    aux=next(it)
    while cond(aux):
            yield(aux)
            aux=next(it)

n=5000
a=squares()
h=take_while(lambda n: n<100, a)

d=first(n,a)

f=filter(lambda h:  str(n) == str(n)[::-1],a)
for i in range(n):
    print(next(f))
