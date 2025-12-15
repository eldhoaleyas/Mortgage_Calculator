import streamlit as st

def mortgage_calculator(loan_amount, monthly_interest_rate, number_of_payments):
    monthly_payment = loan_amount * (monthly_interest_rate *
     (1 + monthly_interest_rate) ** number_of_payments)/((1 + monthly_interest_rate) ** number_of_payments - 1)
    Total_payment = monthly_payment * number_of_payments
    Total_interest = Total_payment - loan_amount

    return monthly_payment, Total_payment, Total_interest

st.title("Mortgage Calculator")

with st.form("order_form"):
    Home_price = st.number_input("Enter the home price:", min_value=0.0, format="%.2f")
    down_payment = st.number_input("Enter the down payment amount:", min_value=0.0, format="%.2f")
    annual_interest_percentage = st.number_input("Enter the annual interest rate (in %):", min_value=0.0, format="%.2f")
    loan_term_years = st.number_input("Enter the loan term (in years):", min_value=1, format="%d")  
    submit_button = st.form_submit_button("Calculate Mortgage")
    if submit_button:
        loan_amount = Home_price - down_payment
        monthly_interest_rate = (annual_interest_percentage / 100) / 12
        number_of_payments = int(loan_term_years) * 12

        monthly_payment, Total_payment, Total_interest = mortgage_calculator(loan_amount, monthly_interest_rate, number_of_payments)

        st.write(f"Loan Amount: {loan_amount:.2f}")
        st.write(f"Your monthly mortgage payment is: {monthly_payment:.2f}")
        st.write(f"Total payment over the life of the loan: {Total_payment:.2f}")
        st.write(f"Total interest paid over the life of the loan: {Total_interest:.2f}")

