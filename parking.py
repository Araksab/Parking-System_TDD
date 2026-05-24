def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
    if parking_duration > 24:
        return "Invalid"
    if is_public_holiday:
        return 15
    if parking_duration < 1:
        return 0

    base_fee = 0
    if vehicle_type.lower() == 'motorcycle':
        base_fee = 2
    elif vehicle_type.lower() == 'car':
        base_fee = 5
    elif vehicle_type.lower() == 'truck':
        base_fee = 10

    surcharge = 3 if day_type.lower() == 'weekend' else 0
    return base_fee + surcharge