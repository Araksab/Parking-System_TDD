from parking import calculate_parking_fee

def test_public_holiday_flat_rate():
    # Menguji aturan: Public holiday flat rate = $15 for all vehicles
    assert calculate_parking_fee('car', 5, 'weekday', True) == 15