import sys
class Stock:
    def __init__(self, name, quantity=0, price = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __repr__(self):
        return f"Stock(name='{self.name}', quantity={self.quantity}, price= {self.price})"

    def __add__(self, other):
        if isinstance(other, Stock):
            return Stock(self.name, self.quantity + other.quantity, self.price)
        else:
            print(f"TypeError: unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")
            exit(1)


    def __sub__(self,other):
        if isinstance(other,Stock):
            if other.quantity > self.quantity:
                print(f"Can\'t reduce the '{self.name}' stock quantity {self.quantity} by {other.quantity}.")
            else:
                return Stock(self.name, self.quantity - other.quantity, self.price)
        else:
            print(f"TypeError: unsupported operand type(s) for i: '{type(self)}' and '{type(other)}'")
            exit(1)
    
    def __mul__(self):
        return self.price * self.quantity
    
    
