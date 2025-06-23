

class Singleton:
    """ You want to make sure that a class has only one instance throughout the entire program.
    Example: database connection pool, logging service, configuration manager."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)

