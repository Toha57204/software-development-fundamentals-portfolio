"""Calculate an order discount based on quantity."""

# ITAP1001 Software Development Fundamentals
# Lesson 1 practical activity


def calculate_discount(quantity: int) -> int:
    """Return the discount percentage for the supplied quantity."""
    if quantity < 10:
        return 5

    if quantity < 50:
        return 10

    if quantity < 100:
        return 15

    return 20


def main() -> None:
    """Ask for a quantity and display the applicable discount."""
    print("Quantity Discount Calculator")
    print("----------------------------")

    try:
        quantity = int(input("Enter the order quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        discount = calculate_discount(quantity)

        print(f"Order quantity: {quantity}")
        print(f"Applicable discount: {discount}%")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
