def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
    if is_public_holiday:
        return 15