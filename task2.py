import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Generates a list of unique random numbers.
    """

    if (
        min_num < 1
        or max_num > 1000
        or min_num > max_num
        or quantity < 1
        or quantity > (max_num - min_num + 1)
    ):
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)

    return sorted(numbers)


# Example usage
lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Your lottery numbers:", lottery_numbers)
