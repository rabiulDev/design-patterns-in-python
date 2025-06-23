
class LightOnCommand:

    """ Encapsulate operations as objects so they can be executed later, queued, or undone.
    Example: Django management commands, Celery tasks. """

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class Light:
    def on(self): print("Light ON")
    def off(self): print("Light OFF")

command = LightOnCommand(Light())
command.execute()