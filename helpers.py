from datetime import date, timedelta


def create_delivery_date(delta: int=1) -> str:
    date_today = date.today()
    delivery_date = date_today + timedelta(days=delta)
    formatted_delivery_date = delivery_date.strftime("%d.%m.%Y")
    return formatted_delivery_date
