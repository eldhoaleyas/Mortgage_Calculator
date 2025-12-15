# Mortgage_Calculator

Formula 

M = P * ( r * (1 + r)^n ) / ( (1 + r)^n - 1 )

$$Where:

M = Total monthly payment
P = Principal loan amount (Home Price - Down Payment)
r = Monthly interest rate (Annual Rate / 12)
n = Number of payments (Loan Term in Years $\times$ 12)

monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)