
## Bahttext
Tool to convert currency number to Thai text number

## Installation
```
pip install py3bahttext
```

## Usage

```
>>> from py3bahttext import bahttext
>>> number = 12345.21
>>> print bahttext(number)
หนึ่งหมื่นสองพันสามร้อยสี่สิบห้าบาทยี่สิบเอ็ดสตางค์
>>> 
```

## Contribution

Any bug fixes are welcomed.

Use `pytest` to confirm sanity of unit test

```bash
$ pip install pytest

... fix bugs, add some tests, and then

$ pytest test_py3bhattext.py
```