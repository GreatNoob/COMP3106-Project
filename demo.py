a = [True]

def try_yield(l):
    for i in range(10):
        l[0] = True
        yield None
        l[0] = False

for i in try_yield(a):
    print(a[0])
