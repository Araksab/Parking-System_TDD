def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
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
    
