from main import calculate_parking_fee

# TC02: Tarif dasar Motor (3 jam, Weekday, Bukan Libur) -> Output: 2
def test_tc02_base_rate_motorcycle():
    fee = calculate_parking_fee("motorcycle", 3, "weekday", False)
    assert fee == 2

# TC03: Tarif dasar Mobil (5 jam, Weekday, Bukan Libur) -> Output: 5
def test_tc03_base_rate_car():
    fee = calculate_parking_fee("car", 5, "weekday", False)
    assert fee == 5

# TC04: Tarif dasar Truk (12 jam, Weekday, Bukan Libur) -> Output: 10
def test_tc04_base_rate_truck():
    fee = calculate_parking_fee("truck", 12, "weekday", False)
    assert fee == 10

# TC05: Tambahan tarif akhir pekan untuk Mobil (4 jam, Weekend, Bukan Libur) -> Output: 8 (5 + 3)
def test_tc05_weekend_surcharge_car():
    fee = calculate_parking_fee("car", 4, "weekend", False)
    assert fee == 8

# TC07: Tarif pukul rata hari libur nasional (Motor, 6 jam, Weekday, Libur) -> Output: 15
def test_tc07_public_holiday_flat_rate():
    fee = calculate_parking_fee("motorcycle", 6, "weekday", True)
    assert fee == 15