# sukurti programa kuria paleidus priimtu 2 parametrus(islaidas ir iplaukas eurais)
#Programa turi paskaiciuoti islaidu ir iplauku menesinius  vidurkius
#Turi paskaiciuoti dienos vidurkius
# Turi paskaiciuoti pajamu ir islaidu procentini santyki

# Pajamu ketvircio rezultatus
# Pusmecio islaidu rezultatus

import logging

logging.basicConfig(filename='mini_budget.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class Accountant:
    def monthly_average(self, amount: float) -> float:
        logging.INFO(f"Receive amont of monthly averages calculations: {amount}  ")
        return amount / 12
    
    def daily_average(self, amount: float) -> float:
        return amount / 365
    
    def calculate_ratio(self, income: float, expenses: float) -> float:
        return(income / expenses, 2)

class Income(Accountant):
    def __init__(self, income: float):
        self.income = income
    
    def quarter_income(self) -> float:
        return self.income / 4

class Expenses(Accountant):
    def __init__(self, expenses: float):
        self.expenses = expenses
    
    def half_year_expenses(self) -> float:
        return self.expenses / 2
   
def main() -> None:
    income = float(input("Enter your yearly income: "))
    expenses = float(input("Enter your yearly expenses: "))
    logging.info(f"Log income amount {income}")
    logging.info(f"Log expenses amount {expenses}")
    inc = Income(income)
    exp = Expenses(expenses)
    print(f"Quarter income is: {inc.quarter_income()}")
    print(f"Daily average of expenses is: {inc.daily_average(expenses)}")
    


if __name__=='__main__':
    main()
    