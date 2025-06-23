class Parser:
    def parse(self, data):
        pass

class CSVParser(Parser):
    def parse(self, data):
        print("Parsing CSV")

class JSONParser(Parser):
    def parse(self, data):
        print("Parsing JSON")

class ParserFactory:
    """ You have multiple classes to instantiate, but don’t want to write lots of if else in the client code.
    Example: You support multiple payment gateways — PayPal, Stripe, etc. """

    @staticmethod
    def get_parser(file_type):
        if file_type == "csv":
            return CSVParser()
        elif file_type == "json":
            return JSONParser()
        else:
            raise ValueError("Unknown file type")

parser = ParserFactory.get_parser("json")
parser.parse("data")
