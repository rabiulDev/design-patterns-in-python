class Publisher:

    """ When one object changes state, automatically notify all interested parties.
    Example: Django signals, notifications, WebSocket broadcasts. """

    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self, data):
        for sub in self.subscribers:
            sub(data)

def send_email(data): print(f"Email: {data}")
def send_sms(data): print(f"SMS: {data}")

pub = Publisher()
pub.subscribe(send_email)
pub.subscribe(send_sms)

pub.notify("Order Created")
