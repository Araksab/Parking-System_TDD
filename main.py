def calculate_parking_fee(vehicle_type: str, parking_duration: float, day_type: str, is_public_holiday: bool) -> float:
    vehicle = vehicle_type.strip().lower()
    day = day_type.strip().lower()

    if parking_duration > 24:
        return -1

    if parking_duration < 1:
        return 0

    if is_public_holiday:
        return 15

    if vehicle_type == "motorcycles":
        fee = 2
    elif vehicle_type == "cars":
        fee = 5
    elif vehicle_type == "trucks":
        fee = 10
    else:
        return -1

    if day_type == "weekday":
        fee = fee
    elif day_type == "weekend":
        fee += 3
    else:
        return -1
    
    return fee
    
