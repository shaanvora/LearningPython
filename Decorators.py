#created a decorator which prints out some information on the function execution


from datetime import datetime

def log_time(func):
    def new_function(*args,**kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:',kwargs)
        start = datetime.now().time().microsecond
        run_function = func(*args,**kwargs)
        finish = datetime.now().time().microsecond
        print('Time taken to run function:' ,(finish - start))
        return run_function
    return new_function


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

@log_time
def non_recursive_fibonacci(n):
    first = 0
    second = 1
    x = 3
    if n == 1:
        return first
    elif n == 2:
        return second
    for x in range(n-2):
        sumofpervioustwo = first + second
        first = second
        second = sumofpervioustwo
    return sumofpervioustwo

pos = 100
print(non_recursive_fibonacci(pos))
testing = log_time(non_recursive_fibonacci)
print(testing(pos))


somethingelse = log_time(lambda x: x*x)
print(somethingelse(10))
