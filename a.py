# import copy
# a=[1,2,3,4,['a','b']]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# a.append(5)
# a[4].append('c')
# print(a)
# print(b)
# print(c)
# print(d)


# def my_d(func):
#     def inner(*args,**kwargs):
#         inner.i += 1
#         return func(*args,**kwargs)
#     inner.i=0
#     return inner
# @my_d
# def test():
#     pass
# test()
# test()
# test()
# print(test.i)

# def mu():
#     return [lambda x:i * x for i in range(4)]
# print([m(3) for m in mu()])

# print('{1:<5}'.format('a','b'))


# w= 'hello'
# v=('a','e','i','o','u')
# z= [i for i in w for j in v if i in j]
# print(z)

# import re
# a= re.compile('0-9')
# print(a.findall('3 trees'))
# print(a)

# with open("a.txt",'r') as f:
#     print(f.name,f.mode, f.closed)
#
#     f.size


# def g(m):
#     if m<1 or m>12:
#         raise ValueError("in")
#     print(m)
# g(6)

# import json
# json.dumps({1,2,4,5})

# for i in range(0):
#
#     print(i)


# import re
# print('search'.find('S'))