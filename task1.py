from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Returns the number of days between the given date and today.
    """

    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        difference = today - given_date

        return difference.days

    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return None


# Example usage
print(get_days_from_today("2020-10-09"))
