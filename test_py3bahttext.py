from py3bahttext import bahttext


def test_input_integer_one_digit_can_convert():
    assert(bahttext(0.0) == 'ศูนย์บาทถ้วน')
    assert(bahttext(1.0) == 'หนึ่งบาทถ้วน')
    assert(bahttext(2.0) == 'สองบาทถ้วน')
    assert(bahttext(5.0) == 'ห้าบาทถ้วน')

def test_number_in_multiple_could_show_sip():
    assert(bahttext(10.0) == 'สิบบาทถ้วน')
    assert(bahttext(20.0) == 'ยี่สิบบาทถ้วน')
    assert(bahttext(50.0) == 'ห้าสิบบาทถ้วน')
    assert(bahttext(11.0) == 'สิบเอ็ดบาทถ้วน')
    assert(bahttext(15.0) == 'สิบห้าบาทถ้วน')

def test_input_one_interger_wth_decimal_can_convert():
    assert(bahttext(1.10) == 'หนึ่งบาทสิบสตางค์')
    assert(bahttext(1.01) == 'หนึ่งบาทหนึ่งสตางค์') # this bug is fixes from bahttext
    assert(bahttext(1.02) == 'หนึ่งบาทสองสตางค์')
    assert(bahttext(1.03) == 'หนึ่งบาทสามสตางค์')
    assert(bahttext(2.50) == 'สองบาทห้าสิบสตางค์')
    assert(bahttext(3.75) == 'สามบาทเจ็ดสิบห้าสตางค์')

def test_number_ending_with_one_could_show_edd():
    assert(bahttext(4.81) == 'สี่บาทแปดสิบเอ็ดสตางค์')

def test_number_start_with_two_could_show_yee():
    assert(bahttext(2.21) == 'สองบาทยี่สิบเอ็ดสตางค์')

def test_number_hundred_should_show_roi():
    assert(bahttext(100.0) == 'หนึ่งร้อยบาทถ้วน')
    assert(bahttext(101.0) == 'หนึ่งร้อยหนึ่งบาทถ้วน')
    assert(bahttext(200.0) == 'สองร้อยบาทถ้วน')
    assert(bahttext(201.0) == 'สองร้อยหนึ่งบาทถ้วน')

def test_number_thoundsand_should_show_pan():
    assert(bahttext(1000.0) == 'หนึ่งพันบาทถ้วน')
    assert(bahttext(2000.10) == 'สองพันบาทสิบสตางค์')
    assert(
        bahttext(3211.51) == 'สามพันสองร้อยสิบเอ็ดบาทห้าสิบเอ็ดสตางค์')
    assert(bahttext(8000.31) == 'แปดพันบาทสามสิบเอ็ดสตางค์')

def test_number_ten_thoundsand_should_show_muern():
    assert(bahttext(30000.0) == 'สามหมื่นบาทถ้วน')
    assert(
        bahttext(98765.10) == 'เก้าหมื่นแปดพันเจ็ดร้อยหกสิบห้าบาทสิบสตางค์')
    assert(
        bahttext(30211.21) == 'สามหมื่นสองร้อยสิบเอ็ดบาทยี่สิบเอ็ดสตางค์')

def test_number_hundred_thoundsand_should_show_saan():
    assert(bahttext(800000.0) == 'แปดแสนบาทถ้วน')
    assert(
        bahttext(258065.81) == 'สองแสนห้าหมื่นแปดพันหกสิบห้าบาทแปดสิบเอ็ดสตางค์')

def test_number_million_should_show_laan():
    assert(bahttext(3500000.0) == 'สามล้านห้าแสนบาทถ้วน')

def test_number_multiple_million_should_show_multiple_laan():
    assert(bahttext(12000000.0) == 'สิบสองล้านบาทถ้วน')
    assert(bahttext(21000000.0) == 'ยี่สิบเอ็ดล้านบาทถ้วน')
    assert(
        bahttext(51000000000000.51) == 'ห้าสิบเอ็ดล้านล้านบาทห้าสิบเอ็ดสตางค์')
    assert(
        bahttext(10000000680000.51) == 'สิบล้านล้านหกแสนแปดหมื่นบาทห้าสิบเอ็ดสตางค์')

def test_negative_minus_prefix_number_should_print_loob():
    assert(bahttext(-1.10) == 'ลบหนึ่งบาทสิบสตางค์')
    assert(bahttext(-1000.0) == 'ลบหนึ่งพันบาทถ้วน')
    assert(
        bahttext(-258065.81) == 'ลบสองแสนห้าหมื่นแปดพันหกสิบห้าบาทแปดสิบเอ็ดสตางค์')
