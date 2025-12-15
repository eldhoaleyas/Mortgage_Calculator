# monthly_payment = loan_amount * (monthly_interest_rate *
#  (1 + monthly_interest_rate) ** number_of_payments) / 
# ((1 + monthly_interest_rate) ** number_of_payments - 1)

def mortgage_calculator(loan_amount, monthly_interest_rate, number_of_payments):
    monthly_payment = loan_amount * (monthly_interest_rate *
     (1 + monthly_interest_rate) ** number_of_payments)/((1 + monthly_interest_rate) ** number_of_payments - 1)

    print(f"Your monthly mortgage payment is: {monthly_payment:.2f}")
    print(f"Total payment over the life of the loan: {monthly_payment * number_of_payments:.2f}")
    print(f"Total interest paid over the life of the loan: {(monthly_payment * number_of_payments) - loan_amount:.2f}")

if __name__ == "__main__":
    Home_price = input("Enter the home price: ")
    down_payment = input("Enter the down payment amount: ")
    loan_amount = float(Home_price) - float(down_payment)
    print(f"Loan Amount: {loan_amount}")
    annual_interest_percentage = input("Enter the annual interest rate (in %): ")
    monthly_interest_rate = (float(annual_interest_percentage) / 100) / 12
    number_of_payments = int(input("Enter the loan term (in years): ")) * 12

    mortgage_calculator(loan_amount, monthly_interest_rate, number_of_payments)