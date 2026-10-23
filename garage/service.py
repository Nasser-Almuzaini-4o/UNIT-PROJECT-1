import calendar
from datetime import date

SERVICE_RULES = {
    "Oil change": {"km": 5000, "months": 6},
    "Filters": {"km": 10000, "months": 12},
    "Brakes": {"km": 20000, "months": None},
    "Tires": {"km": 40000, "months": None},
}

SOON_KM = 500    
SOON_DAYS = 30   



def is_valid_phone(phone):
    """A mobile number is valid only if it consists of exactly 10 English digits. """
    return phone.isascii() and phone.isdigit() and len(phone) == 10


def is_valid_year(year):
    """ The year of manufacture is valid if it is between 1990 and the coming year."""
    return 1990 <= year <= date.today().year + 1



def create_vehicle(plate, owner, car):
    """
    owner: {"name", "phone"}
    car:   {"make", "model", "year", "color", "fuel", "mileage", "vin"}
    """
    return {"plate": plate, "owner": owner, "car": car, "services": []}


def add_service(vehicle, service_type, mileage, cost, technician, notes="", service_date=None):
    """
   The vehicle maintenance log shows the current mileage if the new mileage is higher. 
   ValueError is advised if the mileage or cost is negative.
    """
    if mileage < 0 or cost < 0:
        raise ValueError("Mileage and cost cannot be negative.")
    record = {
        "date": (service_date or date.today()).isoformat(),
        "type": service_type,
        "mileage": mileage,
        "cost": cost,
        "technician": technician,
        "notes": notes,
    }
    vehicle["services"].append(record)
    vehicle["car"]["mileage"] = max(vehicle["car"]["mileage"], mileage)
    return record


def total_cost(vehicle):
    """The total cost of all maintenance performed on the vehicle."""
    return sum(s["cost"] for s in vehicle["services"])



def add_months(start, months):
    """Adds months to a date (e.g., January 31 + 1 month = February 28)."""
    index = start.month - 1 + months
    year = start.year + index // 12
    month = index % 12 + 1
    day = min(start.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def _get_status(remaining_km, due_date, today):
    """
    Specifies the maintenance status:    
    """
    if remaining_km <= 0 or (due_date and today >= due_date):
        return "OVERDUE"
    if remaining_km <= SOON_KM or (due_date and (due_date - today).days <= SOON_DAYS):
        return "SOON"
    return "OK"


def get_next_services(vehicle, today=None):
    """
   Calculates the next scheduled maintenance for each type based on SERVICE_RULES. 
    """
    today = today or date.today()
    current_km = vehicle["car"]["mileage"]
    results = []

    for name, rule in SERVICE_RULES.items():
        records = [s for s in vehicle["services"] if s["type"] == name]

        if not records:
            results.append({
                "service": name, "last_date": None, "last_mileage": None,
                "due_mileage": None, "due_date": None, "remaining_km": None,
                "status": "NO RECORD",
            })
            continue

        last = max(records, key=lambda s: (s["date"], s["mileage"]))
        due_km = last["mileage"] + rule["km"]
        due_date = None
        if rule["months"]:
            due_date = add_months(date.fromisoformat(last["date"]), rule["months"])
        remaining = due_km - current_km

        results.append({
            "service": name, "last_date": last["date"], "last_mileage": last["mileage"],
            "due_mileage": due_km, "due_date": due_date, "remaining_km": remaining,
            "status": _get_status(remaining, due_date, today),
        })

    return results