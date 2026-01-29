import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class NegativeNumberError(Exception):
    pass


def divide_numbers(a, b):
    try:
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")

        result = a / b

    except ZeroDivisionError:
        logging.error("Division by zero error")
        print("❌ Error: Cannot divide by zero")

    except ValueError:
        logging.error("Invalid input type")
        print("❌ Error: Please enter valid numbers")

    except NegativeNumberError as e:
        logging.error(e)
        print(f"❌ Error: {e}")

    except Exception as e:
        logging.error(e)
        print("❌ Unexpected error occurred")

    else:
        print("✅ Result:", result)

    finally:
        print("✔ Execution completed")


# ---- Simulating runtime errors ----
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    divide_numbers(x, y)

except Exception as e:
    logging.error(e)
    print("❌ Program crashed due to invalid input")