# sukurti programa kuria paleidus priimtu 2 parametrus(islaidas ir iplaukas eurais)
#Programa turi paskaiciuoti islaidu ir iplauku menesinius  vidurkius
#Turi paskaiciuoti dienos vidurkius
# Turi paskaiciuoti pajamu ir islaidu procentini santyki

# Pajamu ketvircio rezultatus
# Pusmecio islaidu rezultatus

#viska suloginti 

import logging
from datetime import date, datetime

logging.basicConfig(filename='mini_budget.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

ACCOUNT_FILE = "accounting.txt"

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
    write_info_to_file(f"Accounting year: {datetime.now().year}, \n ")
    write_info_to_file(f"Our yearly income: {income}, \n ")
    write_info_to_file(f"Our yearly expenses: {expenses}, \n ")
    logging.info(f"Log income amount {income}")
    logging.info(f"Log expenses amount {expenses}")
    inc = Income(income)
    exp = Expenses(expenses)
    write_info_to_file(f"Our quaterly income: {inc.quarter_income()}, \n ")
    write_info_to_file(f"Our daily expenses: {inc.daily_average(expenses)}, \n ")
    
    
    print(f"Quarter income is: {inc.quarter_income()}")
    print(f"Daily average of expenses is: {inc.daily_average(expenses)}")
  
    
def write_info_to_file(data:str) -> None:
    with open(ACCOUNT_FILE, 'a') as f:
        f.write(data)
        
if __name__=='__main__':
    main()
 