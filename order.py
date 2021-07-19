from mysqlconnection import connectToMySQL

class Order():

    def __init__(self, data):
        self.id = data['id']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zip_code = data['zip_code']
        self.cost = data['cost']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders;"

        results = connectToMySQL('orders_demo').query_db(query)

        orders = []

        for item in results:
            orders.append(Order(item))

        return orders

    @classmethod
    def create_order(cls, data):
        query = "INSERT INTO orders (address, city, state, zip_code, cost) VALUES (%(address)s, %(city)s, %(state)s, %(zip_code)s, %(cost)s);"

        return connectToMySQL('orders_demo').query_db(query, data)



        

