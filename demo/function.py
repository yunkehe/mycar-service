def foo(x):
     print(locals())

foo(1)

def outer(some_func):
     def inner():
         print("before some_func")
         ret = some_func()  # 1
         return ret + 1
     return inner

@outer
def foo2():
     return 1


# decorated = outer(foo2)  # 2
# print(decorated())
print('@outer result --> %s' % foo2())
