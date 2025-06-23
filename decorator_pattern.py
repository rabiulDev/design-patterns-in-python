def my_decorator(func):
    """ You want to add functionality to existing functions or classes without modifying them.
    Example: Logging, authentication, caching, permission checking. """

    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")

    return wrapper


@my_decorator
def greetings(name):
    print(f"Hello {name}")


greetings("BoomDevs")