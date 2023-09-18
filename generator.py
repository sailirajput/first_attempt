#generator
'''def gen(n):
    for i in range(n):
        yield i

obj1=gen(4)
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))'''

#iterable
l=[1,2,3]
obj=iter(l)
print(next(obj))
print(next(obj))
print(next(obj))


