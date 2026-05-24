from parking import calculate_parking_fee

# TC01: Dibawah 1 jam (Mobil, 0.5 jam, Weekday, Bukan Libur) -> Output: 0
def test_tc01_under_one_hour_is_free():
    fee = calculate_parking_fee("car", 0.5, "weekday", False)
    assert fee == 0