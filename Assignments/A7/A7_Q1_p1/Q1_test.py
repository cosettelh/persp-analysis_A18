# Cosette L. Hampton 
# A7 - Question 1 test file

import Q1 

def test_sf(): 
    assert Q1.smallest_factor(15) == 3, "failed on positive odd integers" 
    assert Q1.smallest_factor(6) == 2, "failed on integers less than 8" 
    assert Q1.smallest_factor(32) == 2