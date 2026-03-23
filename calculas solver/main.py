import streamlit as st
import sympy as sp

x = sp.symbols('x')


def explain_derivative(expr):
    expr = sp.expand(expr)
    terms = expr.as_ordered_terms()
    steps = []

    for term in terms:
        d = sp.diff(term, x)
        steps.append(f"d/dx({term}) = {d}")

    return steps


def explain_integral(expr):
    expr = sp.expand(expr)
    terms = expr.as_ordered_terms()
    steps = []

    for term in terms:
        i = sp.integrate(term, x)
        steps.append(f"∫({term}) dx = {i}")

    return steps



st.title("Calculus Solver")
st.caption("Use * for multiplication and ** for powers (e.g., x**2 + 3*x)")

operation = st.selectbox("Choose operation", ["Derivative", "Integral"])

if operation == "Derivative":
    expr_input = st.text_input("Enter expression")

    if st.button("Solve"):
        try:
            expr = sp.sympify(expr_input)
            result = sp.diff(expr, x)

            st.subheader("Steps:")
            steps = explain_derivative(expr)

            for i, step in enumerate(steps, 1):
                st.write(f"Step {i}: {step}")

            st.success(f"Final Answer: {result}")

        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Integral":
    expr_input = st.text_input("Enter expression")
    lower = st.text_input("Lower limit (optional)")
    upper = st.text_input("Upper limit (optional)")

    if st.button("Solve"):
        try:
            expr = sp.sympify(expr_input)

            if lower and upper:
                result = sp.integrate(expr, (x, float(lower), float(upper)))
            else:
                result = sp.integrate(expr, x)

            st.subheader("Steps:")
            steps = explain_integral(expr)

            for i, step in enumerate(steps, 1):
                st.write(f"Step {i}: {step}")

            st.success(f"Final Answer: {result}")

        except Exception as e:
            st.error(f"Error: {e}")