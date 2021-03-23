class Tax:
    tax_rate = 0.0825
    def __init__(self, number):
        self.original = number
        self.tax = self.original* Tax.tax_rate
        self.total = self.original - self.tax
print('Enter an item to get the taxed amount')
item_1 = Tax(float(input()))
print(f"This is the item amount before tax: {item_1.original}")
print(f"This is the item taxation: {item_1.tax}")
print(f"Final amount is {item_1.total}")
