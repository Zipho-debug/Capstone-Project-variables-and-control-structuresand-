import math 

def main():
    print("Investment - to calculate the amount of interest you'll earn on an investment")
    print("Bond - to calculate the amount of interest you'll pay on a home loan")

    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if choice == "investment":
        investment()
    elif choice == "bond":
        bond() # type: ignore
    else:
        print("Invalid input. Please enter either 'investment' or 'bond'.")

def investment():
    """
    Prompts the user for investment details and calculates the future value of the investment
    based on the type of interest (simple or compound).
    The function asks the user to input the following:
    - The principal amount (initial deposit)
    - The annual interest rate (as a percentage)
    - The number of years the money is to be invested
    - The type of interest (simple or compound)
    Depending on the type of interest, it calculates and prints the future value of the investment.
    Returns:
        None
    """
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing for: "))
    interest_type = input("Enter the type of interest (simple or compound): ").lower()
    if interest_type == "simple":
        def simple_interest(principal, interest_rate, years):
            r = interest_rate / 100
            A = principal * (1 + r * years)
            print(f"Your investment will be worth R{A:.2f} after {years} years.")
        
        simple_interest(principal, interest_rate, years)
    elif interest_type == "compound":
        def compound_interest(principal, interest_rate, years):
            r = interest_rate / 100
            A = principal * math.pow((1 + r), years)
            print(f"Your investment will be worth R{A:.2f} after {years} years.")
        
        compound_interest(principal, interest_rate, years)
    else:
        print("Invalid input. Please enter either 'simple' or 'compound'.")  
        print("Invalid input. Please enter either 'simple' or 'compound'.")
    
    def bond():
        present_value = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        months = int(input("Enter the number of months you plan on taking to repay the bond: "))
            
        monthly_interest_rate = annual_interest_rate / 12 / 100 
        repayment = (monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, -months))
        print(f"Your monthly bond repayment will be R{repayment:.2f}.")
