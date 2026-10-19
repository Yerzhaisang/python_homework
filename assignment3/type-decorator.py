# Task 2: A Decorator that Takes an Argument


def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator


# Task 2: returns the integer 5, converted to str by the decorator
@type_converter(str)
def return_int():
    return 5


# Task 2: returns a non-numeric string, int() conversion will raise ValueError
@type_converter(int)
def return_string():
    return "not a number"


# Task 2: mainline
y = return_int()
print(type(y).__name__)  # This should print "str"
try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")  # This is what should happen
