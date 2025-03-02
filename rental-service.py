class vehicle :
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.__rental_price_per_day=rental_price_per_day
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day
    def set_rental_price_per_day(self,newPrice):
        self.__rental_price_per_day=newPrice
    def display_info(self):
       return(
            f"{self.__class__.__name__}:{self.brand} {self.model},Year:{self.year},"
            f"Renatal Price:${self.__rental_price_per_day}/day"
        )