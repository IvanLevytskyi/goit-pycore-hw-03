from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Returns a list of users who should be congratulated
    within the next week.
    """

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(
            user["birthday"],
            "%Y.%m.%d"
        ).date()

        # Birthday in the current year
        birthday_this_year = birthday.replace(year=today.year)

        # If the birthday has already passed, use next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        delta_days = (birthday_this_year - today).days

        # Check if the birthday is within 7 days
        if 0 <= delta_days <= 7:

            congratulation_date = birthday_this_year

            # If Saturday
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            # If Sunday
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date":
                    congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Upcoming congratulations:")
print(upcoming_birthdays)
