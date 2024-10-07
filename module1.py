gravity = 9.8


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def square_elements(lst):
    '''
    Takes a list as an argument, calculates square of each element of that list and returns a list
    '''
    return list(map(lambda x: x**2, lst))


if __name__ == '__main__': # It means that the file is getting executed directly
    a = 9
    res = is_even(a)
    if res == True:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")


"""
There is an internal variable in Python => __name__ (dunder name variable)
For every .py file in Python, the Python interpreter creates this variable __name__
The value for this variable is assigned by the interpreter depending on how the file is getting executed
If we execute the file directly, __name__ = '__main__'
If we import the file as a module, __name__ = <module name> as a str (without dunder)

When we run module1.py =>
For module1.py, __name__ = '__main__'

When we run program.py =>
For program.py, __name__ = '__main__'
For module1.py, __name__ = 'module1'
"""