class vehicle :
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.__rental_price_per_day=rental_price_per_day
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day
    