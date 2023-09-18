def simple():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
'''save=simple()
temp=iter(save)
print(next(temp))
print(next(temp))'''
'''def simple():
    for x in range(10):
        yield x
save=simple()
temp=iter(save)
print(next(temp))'''
'''def simple():
    for x in range(10):
        yield x
save=simple()
for data in save:
    print(data)
for data in save:
    print(data)'''
def imp():
    for x in range(10):
        yield x
save=imp()
save='chetu india'
temp=iter(save)
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
if(next(temp)=='t'):
    print("ok fine")
