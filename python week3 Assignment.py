

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount if it's 20% or higher.
    :param price: float, original price of the item
    :param discount_percent: float, discount percentage
    :return: float, final price after discount or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")

