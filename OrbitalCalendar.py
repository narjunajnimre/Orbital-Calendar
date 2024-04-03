import datetime
from enum import Enum

class Week(Enum):
    SPRING = "Spring Week"
    SUMMER = "Summer Week"
    FALL = "Fall Week"
    WINTER = "Winter Week"

class OrbitalCalendar:
    MONTHS = ["Month " + str(i+1) for i in range(13)]
    DAYS = ["Corday", "Devday", "Fooday", "Knoday", "Wilday", "Artday", "The Sabbath"]

    def __init__(self, year=None):
        self.current_month = 0
        self.year = year if year else datetime.datetime.now().year
        self.current_date = datetime.date(self.year, 1, 1)  # Start from the first day of the year

    @property
    def is_leap(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def display_month(self):
        print(f"\n{self.MONTHS[self.current_month]}, {self.year}")
        print(f"==============================")
        for i, week in enumerate(Week):
            print(f"Week {i+1} = {week.value}")
            days = self.DAYS.copy()
            if self.is_leap and self.current_month == 2 and i == 0:  # Leap Day on the 4th day of the 3rd month
                days.insert(3, "Leap Day")
            if self.current_month == 12 and i == 3:  # Last Day at the end of Winter Week of the last month
                days.append("Last Day")
            for day in days:
                print(f"{day}: {self.current_date.strftime('%B %d, %Y')}")
                self.current_date += datetime.timedelta(days=1)  # Increment the date
            print()

    def previous_month(self):
        # Subtract the number of days for the current month
        if (self.is_leap and self.current_month == 2) or self.current_month == 12:
            self.current_date -= datetime.timedelta(days=29)
        else:
            self.current_date -= datetime.timedelta(days=28)

        if self.current_month > 0:
            self.current_month -= 1
        else:
            self.current_month = 12
            self.year -= 1

        # Subtract the number of days for the previous month
        if (self.is_leap and self.current_month == 2) or self.current_month == 12:
            self.current_date -= datetime.timedelta(days=29)
        else:
            self.current_date -= datetime.timedelta(days=28)

    def next_month(self):
        if self.current_month < 12:
            self.current_month += 1
        else:
            self.current_month = 0
            self.year += 1

calendar = OrbitalCalendar()
calendar.display_month()

while True:
    command = input("Enter command (p for previous, n for next, q for quit): ")
    if command.lower() == 'p':
        calendar.previous_month()
        calendar.display_month()
    elif command.lower() == 'n':
        calendar.next_month()
        calendar.display_month()
    elif command.lower() == 'q':
        break
    else:
        print("Invalid command. Please enter p, n, or q.")
