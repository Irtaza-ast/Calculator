from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
import streamlit as st

st.subheader("Calculator by Irtaza Ali")
num1 = st.number_input("Enter your first number:", key="num1")
num2 = st.number_input("Enter your second number:", key="num2")
operator = st.write("Enter the operation you want to perform:")
plus = st.button("\+")
minus = st.button("\-")
asterisk = st.button("\*")
backslash = st.button("/")
if plus:
    sum = add(num1, num2)
    st.write(f"Sum of the numbers is: {sum:.2f}")
elif minus:
    dif = subtract(num1, num2)
    st.write(f"Difference of the numbers is: {dif:.2f}")
elif asterisk:
    prod = multiply(num1, num2)
    st.write(f"Product of the numbers is: {prod:.2f}")
elif backslash:
    quot = divide(num1, num2)
    st.write(f"Quotient of the numbers is: {quot:.2f}")
