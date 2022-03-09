import csv

class Item:
    
    #class attribute only when instance attribute is not found
    pay_rate = 0.8 
    all = []

    # Constructor
    def __init__(self,name:str,price:float,quantity=0):
        
        # Run validations to the received arguments
        assert price >=0, f"Price {price} is not greater than zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!"
        assert type(name) == str, f"Name {name} is not an string!"
        assert type(price) == float or int, f"Price {price} is not an float!"
        assert type(quantity) == int, f"Quantity {quantity} is not an float!"

        #assign of self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    # Encasulation (ignore direct access)    
    @property
    # Property Decorator = Read-Only Attributes
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value
    
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value<0:
            raise Exception("The price is negative!")
        self.__price = value
        
    def apply_discount(self):
        # always apply class attribute value, not ideal
        # self.price = self.price*Item.pay_rate
        self.__price = self.__price*self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price +self.__price*increment_value
    
    # Represent
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.__quantity})"

    # class instead of instance self
    @classmethod
    def instantiate_from_csv(cls):
        #r,w,a,r+w
        # with context manager, automatically close the file
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = int(item.get('quantity'))
                )

    # send instance as first argument
    @staticmethod
    def is_integer(num):
        # count out the floats that are point zero
        # For 5.0,10.0 etc
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    
    def calculate_total_price(self):
        return self.__price * self.__quantity
    
    def __connect(self, smpt_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.__name} {self.__quantity} times.
        Regards, 
        JimShapedCoding
        """
    
    def __send(self):
        pass
        
    # Abstraction
    def send_email(self):
        self.__connect("a")
        self.__prepare_body()
        self.__send()
    

        
