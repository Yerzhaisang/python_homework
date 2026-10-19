# Task 1: Writing and Testing a Decorator
import logging

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "")
        return result
    return wrapper


# Task 1: function with no parameters that returns nothing
@logger_decorator
def say_hello():
    print("Hello, World!")


# Task 1: variable positional arguments, returns True
@logger_decorator
def positional_only(*args):
    return True


# Task 1: no positional arguments, variable keyword arguments, returns logger_decorator
@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    # Task 1: mainline calls each of the three functions
    say_hello()
    positional_only(1, "two", 3.0)
    keyword_only(name="Taskali", language="Python")
