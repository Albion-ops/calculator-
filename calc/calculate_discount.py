def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Keep asking until valid input is given
while True:
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        break  # exit loop if inputs are valid
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.\n")

# Call the function
final_price = calculate_discount(price, discount_percent)

# Output result
if discount_percent >= 20:
    print(f"\n✅ Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"\nℹ️ No discount applied. The price remains: {final_price:.2f}")
