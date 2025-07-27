from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    # Add days
    future_date = current_date + timedelta(days=days_to_add)
    # Format as YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    # Ask user for days to add
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
