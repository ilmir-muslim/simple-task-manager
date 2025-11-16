from datetime import datetime

def format_due_date(date_string):
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
        return date.strftime("%d.%m.%Y")
    except ValueError:
        return "Invalid date"
