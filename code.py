import datetime
from collections import defaultdict
from operator import itemgetter

def get_days_between(start_date, end_date):
    days = []
    current = start_date
    while current <= end_date:
        days.append(current)
        current += datetime.timedelta(days=1)
    return days

def get_priority_score(task):
    score = 0
    if task["importance"] == "high":
        score += 2
    elif task["importance"] == "medium":
        score += 1

    # Compare date only
    days_left = (task["deadline"].date() - datetime.datetime.now().date()).days
    if days_left <= 0:
        score += 3
    elif days_left <= 2:
        score += 2
    elif days_left <= 5:
        score += 1

    return score

def allocate_schedule(tasks, daily_limit=4):
    schedule = defaultdict(list)
    today = datetime.datetime.today()

    for task in tasks:
        task["priority"] = get_priority_score(task)
        task["days"] = get_days_between(today.date(), task["deadline"].date())

    # Sort tasks by priority (higher score first)
    tasks.sort(key=itemgetter("priority"), reverse=True)

    for task in tasks:
        hours_left = task["hours"]
        days = task["days"]
        per_day = max(1, hours_left // len(days))

        for day in days:
            if hours_left <= 0:
                break

            assigned_today = sum([t[1] for t in schedule[day]])
            available_time = daily_limit - assigned_today

            if available_time <= 0:
                continue

            to_assign = min(per_day, hours_left, available_time)
            if to_assign > 0:
                schedule[day].append((task["name"], to_assign))
                hours_left -= to_assign

    return schedule

def main():
    tasks = []
    n = int(input("How many subjects/topics do you want to plan? "))

    for _ in range(n):
        name = input("Topic name: ")
        importance = input("Importance (high/medium/low): ").lower()
        while importance not in ("high", "medium", "low"):
            importance = input("Please enter importance as high/medium/low: ").lower()

        deadline_input = input("Deadline (YYYY-MM-DD): ")
        hours = int(input("Estimated hours to study: "))

        try:
            deadline = datetime.datetime.strptime(deadline_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        tasks.append({
            "name": name,
            "importance": importance,
            "deadline": deadline,
            "hours": hours
        })

    schedule = allocate_schedule(tasks)

    print("\n🗓 Study Plan:")
    if not schedule:
        print("No tasks could be scheduled.")
    else:
        for day in sorted(schedule.keys()):
            print(f"\n📅 {day.strftime('%A, %Y-%m-%d')}")
            for topic, hours in schedule[day]:
                print(f"  - {topic}: {hours} hour(s)")

if _name_ == "_main_":
    main()
