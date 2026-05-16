import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the +380XXXXXXXXX format.
    """

    # Remove all characters except digits and +
    sanitized_number = re.sub(r"[^\d+]", "", phone_number)

    # If the number starts with +
    if sanitized_number.startswith("+"):
        return sanitized_number

    # If the number starts with 380
    if sanitized_number.startswith("380"):
        return "+" + sanitized_number

    # In all other cases add +38
    return "+38" + sanitized_number


# Example usage
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050)123-32-34",
    " 0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Normalized phone numbers:")
print(sanitized_numbers)
