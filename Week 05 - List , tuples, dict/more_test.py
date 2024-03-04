from datetime import datetime
day_time = datetime.now()
print(day_time)

week_day = day_time.weekday()
if week_day <5:
    print("Weekday")
else:
    print("weekend")

