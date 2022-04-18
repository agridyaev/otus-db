class Customer:
    def __init__(self, first_name, last_name, email, telephone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone


customer = Customer(
    first_name='Bruce',
    last_name='Wayne',
    email='bruce.wayne@gmail.com',
    telephone='+79213332211'
)
