class PayPalPayment:
    def pay(self, amount):
        print(f"Paying {amount} with PayPal")

class StripePayment:
    def pay(self, amount):
        print(f"Paying {amount} with Stripe")


class Processor:
    """ You have different algorithms that can be swapped at runtime.
    Example: different pricing algorithms, different sorting strategies. """

    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)



processor = Processor(PayPalPayment())
processor.pay(100)

processor = Processor(StripePayment())
processor.pay(200)