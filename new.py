# Bisection mehtod
import timeit
mycode='''def f(x):
    return x**20-x**16-x**8-x

a=1
b=2

tolerance = 1e-6
max_iterations = 100

for i in range(max_iterations):
    c = (a+b)/2
    
    if abs(f(c))<tolerance:
        print(f" Roof found at x={c: 6f}")
        break
    elif f(c)*f(a)<0:
        b=c
    else:
        a=c'''


print (timeit.timeit(stmt = mycode,number = 1))



mycode = '''
def f(x):
    return x**20-x**16-x**8-x

def df(x):
    return 20*x**19-16*x**15-8*x**7-1

x0 = 2
tolerance = 1e-6
max_iterations = 100



for i in range (max_iterations):
    fx = f(x0)
    dfx=df(x0)
    x1=x0-fx/dfx
    if abs(f(x1))<tolerance:
        print(f"Root found at x={x1: 6f}")
        break
    else:
        x0=x1'''
        
print (timeit.timeit(stmt = mycode,number = 1))
