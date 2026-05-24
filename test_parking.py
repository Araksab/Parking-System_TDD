from parking import calculate_parking_fee

def test_public_holiday_flat_rate():
    assert calculate_parking_fee('car', 5, 'weekday', True) == 15

def test_under_one_hour_free():
    assert calculate_parking_fee('motorcycle', 0.5, 'weekday', False) == 0

def test_base_fees():
    assert calculate_parking_fee('motorcycle', 2, 'weekday', False) == 2
    assert calculate_parking_fee('car', 2, 'weekday', False) == 5
    assert calculate_parking_fee('truck', 2, 'weekday', False) == 10

def test_weekend_surcharge():
    assert calculate_parking_fee('car', 2, 'weekend', False) == 8

def test_invalid_duration():
    assert calculate_parking_fee('car', 25, 'weekday', False) == "Invalid"