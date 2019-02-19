#----------------------------------------#
# Title: test_mailroom4.py
# Derived from mailroom4.py
# Claire Yoon,2019-02-18,New file
#----------------------------------------#

import os.path
from mailroom4 import print_list, update_donor, write_thx, get_report, donor_dict, letter_text

def test_write_file():
    for key in donor_dict.keys():
        donor_name = key.split(' ')
        filename = '_'.join(donor_name) + '_Thx_Letter'
        assert os.path.isfile(filename) == True

def test_letter_text():
    assert letter_text("Dwight","Schrute",12345) == "\nDear Dwight Schrute,\n\nOur organization would like to thank you for your donation of $12345 so far.\nOur organization relies on the generosity of donors such as yourself.\n\nThank you once again. \n"

def test_print_list():
    assert print_list() == ['Will Gates', 'Conan Obrien', 'Mark Zucker', 'Jeff Bezos', 'Tom Hardy']

def test_update_donor():
    assert update_donor('Brad Pitt', 30000) == {'Will Gates': [10000, 20000, 300000], 'Conan Obrien': [20000], 'Mark Zucker': [30000, 12000], 'Jeff Bezos': [50000], 'Tom Hardy': [12000, 40000], 'Brad Pitt': [30000.0]}

def test_write_thx():
    assert write_thx("Brad Pitt", 30000) == "\nDear Brad Pitt,\n\nOur organization would like to thank you for your donation of $30000 so far.\nOur organization relies on the generosity of donors such as yourself.\n\nThank you once again. \n"

def test_get_report():
    assert get_report() == [['Will Gates', 330000, 3, 110000.0], ['Conan Obrien', 20000, 1, 20000.0], ['Mark Zucker', 42000, 2, 21000.0], ['Jeff Bezos', 50000, 1, 50000.0], ['Tom Hardy', 52000, 2, 26000.0], ["Brad Pitt", 30000, 1, 30000.0]]

