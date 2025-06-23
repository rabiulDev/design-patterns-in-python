class QueryBuilder:
    """ You want to build complex objects step by step, without messy constructors.
    Example: Building SQL queries, building complex report payloads. """

    def __init__(self):
        self.query = "SELECT * FROM users"

    def where(self, condition):
        self.query += f" WHERE {condition}"
        return self

    def order_by(self, field):
        self.query += f" ORDER BY {field}"
        return self

    def build(self):
        return self.query


query = QueryBuilder().where("id > 10").order_by("created_at").build()
print(query)
