# simple-interest.py
# A simple program to calculate Simple Interest

def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest.
    
    Formula:
        SI = (P * R * T) / 100
    where:
        P = Principal amount
        R = Rate of interest per year
        T = Time period in years
    """
    return (principal * rate * time) / 100


if __name__ == "__main__":
    print("=== Simple Interest Calculator ===")
    
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time in years: "))
        
        interest = calculate_simple_interest(principal, rate, time)
        print(f"\nSimple Interest: {interest:.2f}")
        print(f"Total Amount after {time} years: {principal + interest:.2f}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")
