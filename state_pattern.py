""" Object changes its behavior based on internal state.
Example: order status transitions (pending, paid, shipped)."""

class Order:
    def __init__(self):
        self.state = Pending()

    def next(self):
        self.state = self.state.next()

class Pending:
    def next(self):
        print("Moving to Paid state")
        return Paid()

class Paid:
    def next(self):
        print("Moving to Shipped state")
        return Shipped()

class Shipped:
    def next(self):
        print("Already shipped")
        return self


order = Order()
order.next()
order.next()
order.next()
