# -*- coding: utf-8 -*-
# Convert float decimal number to Thai text number
# Copyright (C) 2014, Morange Solution Co.,LTD.
# All rights reserved. check LICENSE for more detail.
# Seksan Poltree <seksan@morange.co.th>, 2014.

thainum = [u"ศูนย์", u"หนึ่ง", u"สอง", u"สาม",
           u"สี่", u"ห้า", u"หก", u"เจ็ด", u"แปด", u"เก้า"]
thaimulti = [u"", u"สิบ", u"ร้อย", u"พัน", u"หมื่น", u"แสน", u"ล้าน"]


def split_million_sequence(seq):
    mlength = 6
    seq = seq[::-1]
    splited_seq = [seq[i:i + mlength][::-1]
                   for i in range(0, len(seq), mlength)]
    return splited_seq[::-1]


def convert_special_twodigit(int_string):

    baht_string = u''

    if int_string[0] == '1':
        pass
    elif int_string[0] == '2':
        baht_string += u"ยี่"
    elif int_string[0] in "3456789":
        baht_string += thainum[int(int_string[0])]

    if int_string[0] != '0':
        baht_string += u'สิบ'

    if int_string[1] == '0':
        pass
    elif int_string[1] == '1':
        baht_string += u'เอ็ด'
    else:
        baht_string += thainum[int(int_string[1])]

    return baht_string


def convert_multiple_million(int_string, is_million=False):

    baht_string = u''

    # integer number part
    if len(int_string) == 1:
        baht_string += thainum[int(int_string)]

    elif len(int_string) == 2:
        baht_string += convert_special_twodigit(int_string)

    elif len(int_string) in range(3, 7):
        for number_index in range(0, len(int_string) - 2):
            if int(int_string[number_index]) != 0:
                baht_string += thainum[int(int_string[number_index])]
                baht_string += thaimulti[len(int_string) - number_index - 1]

        baht_string += convert_special_twodigit(int_string[-2:])

    return baht_string


def bahttext(input_float):

    baht_string = u''

    float_string = '%0.2f' % input_float
    input_string = str(float_string).split('.')

    int_string = input_string[0]
    decimal_string = input_string[1]

    million_sequence_list = split_million_sequence(int_string)

    million_index = len(million_sequence_list) - 1

    for million_group_string in million_sequence_list:

        is_million = False
        if million_index > 0:
            is_million = True

        baht_string += convert_multiple_million(
            million_group_string, is_million)

        if million_index > 0:
            baht_string += u'ล้าน'
            million_index -= 1

    baht_string += u'บาท'

    # decimal number part
    if int(decimal_string) == 0:
        baht_string += u'ถ้วน'

    else:
        if len(decimal_string) == 1:
            baht_string = thainum[int(decimal_string)]

        elif len(decimal_string) == 2:
            baht_string += convert_special_twodigit(decimal_string)

        baht_string += u'สตางค์'

    return baht_string
