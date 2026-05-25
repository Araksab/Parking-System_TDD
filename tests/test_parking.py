VEHICLE_RATES = {
    "motorcycle": 2,
    "car": 5,
    "truck": 10
}

WEEKEND_SURCHARGE = 3
PUBLIC_HOLIDAY_RATE = 15
MAX_DURATION = 24

def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
    """Calculate parking fee based on vehicle type, duration, and day."""
    if parking_duration > MAX_DURATION:
        raise ValueError("Parking duration above 24 hours is invalid")
    
    if parking_duration < 1:
        return 0
    
    if is_public_holiday:
        return PUBLIC_HOLIDAY_RATE
    
    fee = VEHICLE_RATES[vehicle_type]
    
    if day_type == "weekend":
        fee += WEEKEND_SURCHARGE
    
    return fee