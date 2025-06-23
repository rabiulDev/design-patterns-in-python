class Adapter:
    """ You have existing incompatible interfaces and want them to work together.
    Example: Your new system expects print() method, but your old system has old_api(). """

    def __init__(self, obj):
        self.obj = obj

    def unified_api(self):
        if hasattr(self.obj, "old_api"):
            self.obj.old_api()
        else:
            self.obj.new_api()


class OldSystem:
    @staticmethod
    def old_api():
        print("Old system")

class NewSystem:
    @staticmethod
    def new_api():
        print("New system")


adapter1 = Adapter(OldSystem())
adapter2 = Adapter(NewSystem())

adapter1.unified_api()
adapter2.unified_api()
