
import streamlit as st

# 1. Page configuration
st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# 2. Initialise session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# 3. Dashboard heading
st.title("💰 Personal Expense Tracker")
st.write("Track and manage your daily expenses easily.")

st.divider()

# 4. Add expense form
st.header("➕ Add New Expense")

with st.form("expense_form"):

    description = st.text_input("Expense Description")

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=100.0
    )

    category = st.selectbox(
        "Expense Category",
        ["Food", "Travel", "Shopping",
         "Bills", "Entertainment", "Other"]
    )

    expense_date = st.date_input("Expense Date")

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if description.strip() and amount > 0:

            new_expense = {
                "Description": description,
                "Amount": amount,
                "Category": category,
                "Date": expense_date
            }

            st.session_state.expenses.append(new_expense)

            st.success("Expense added successfully!")

        else:
            st.warning("Please enter a description and valid amount.")

st.divider()

# 5. Expense dashboard
st.header("📊 Expense Dashboard")

if st.session_state.expenses:

    total = sum(
        expense["Amount"]
        for expense in st.session_state.expenses
    )

    count = len(st.session_state.expenses)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Expenses", f"₹{total:,.2f}")

    with col2:
        st.metric("Number of Transactions", count)

    # 6. Display expense history
    st.subheader("📋 Expense History")

    st.dataframe(
        st.session_state.expenses,
        width="stretch"
    )

else:
    st.info("No expenses added yet. Start by adding your first expense!")
