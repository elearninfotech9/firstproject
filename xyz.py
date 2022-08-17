a=100 #global

def f1():
    global a
    a=1000 #local
    b=2000 #local

    print(globals()['a'])

def f2():
    print(a)


f1()
f2()
