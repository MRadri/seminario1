
def square(a):
    for i in a:
        yield i*i

a = [1,2,10,4,5]

d=square(a)
for i in range(len(a)):
    print(next(d))