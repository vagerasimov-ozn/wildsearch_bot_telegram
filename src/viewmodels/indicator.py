from ..helpers import smart_format_number, smart_format_prettify
from .base import BaseViewModel


class Indicator(BaseViewModel):
    def __init__(self, number, units=None, label=None, precise=False):
        self._number_raw = number
        self._units = units
        self._label = label
        self._precise = precise

        if precise is False:
            self._number, self._text_digits = smart_format_number(number)
        else:
            try:
                number = int(number)
                self._number, self._text_digits = smart_format_prettify(number), ''
            except ValueError:
                self._number, self._text_digits = '–', ''

    @property
    def number_raw(self):
        return self._number_raw

    @property
    def number(self):
        return self._number

    @property
    def digits(self):
        return self._text_digits

    @property
    def units(self):
        if self._number == '–':
            return ''
        else:
            return self._units

    @property
    def label(self):
        return self._label
