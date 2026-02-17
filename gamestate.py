class GameState:
    def __init__(self):
        self.salary = 40000.00
        self.monthly_salary = self.salary // 12
        self.in_bank = 2000.00
        self.pet_cost = 0
        self.meal_cost = 200.00
        self.bills_cost = 200.00
        self.rent = 1200.00
        self.monthly_expenses = self.pet_cost + self.meal_cost + self.bills_cost + self.rent
        self.available_cash = self.monthly_salary + self.in_bank - self.monthly_expenses
        self.months_since_start = 0
        self.stocks_owned = {}
        self.points = 0
        
        self.car = "No car"
        self.house = "Starter house"
        self.pets = []
    
    def update_expenses(self):
        self.monthly_expenses = self.pet_cost + self.meal_cost + self.bills_cost + self.rent
    def update_cash(self):
        self.available_cash = self.monthly_salary + self.in_bank - self.monthly_expenses

state = GameState()
