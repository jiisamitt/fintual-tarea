class Stock:

    def __init__(self, name, price):
        pass
    
    def price(self, date):
        pass

class Portfolio:

    def __init__(self):
        self.stocks = [] # List of Stock objects
        
    def profit(self, first_date, last_date):
        # Regular profit
        total_profit = 0
        initial_value = 0
        final_value = 0

        for stock in self.stocks:
            initial_price = stock.price(first_date)
            final_price = stock.price(last_date)
            total_profit += final_price - initial_price
            initial_value += initial_price
            final_value += final_price

        # Annualized return
        delta_days = (last_date - first_date).days
        years = delta_days / 365
        if years > 0 and initial_value > 0:
            annualized_return = (final_value / initial_value) ** (1 / years) - 1
        else:
            annualized_return = 0

        return total_profit, annualized_return # Regular profit, Annualized return