# Cosette L. Hampton 
# A7 - Question 2 test file (same as Q1)

import Q2 

def test_sf(): 
    assert Q2.smallest_factor(15) == 3, "failed on positive odd integers" 
    assert Q2.smallest_factor(6) == 2, "failed on integers less than 8" 
    assert Q2.smallest_factor(32) == 2
    
## Comprehensive unit test for month_length() in Q2 

def test_ml(): 
    assert Q2.month_length("January") == 31, "January has 31 days"
    assert Q2.month_length("February", leap_year = True) == 29, "Feb has 29 days during a leap year"
    assert Q2.month_length("February", leap_year = False) == 28, "Feb has 28 days with no leap year"
    assert Q2.month_length("March") == 31, "March has 31 days"
    assert Q2.month_length("April") == 30, "April has 30 days"
    # and so on...
    assert Q2.month_length("December") == 31, "December has 31 days" 
    assert Q2.month_length("blooper") == None