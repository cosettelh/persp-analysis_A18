# Cosette L. Hampton 
# A7 - Question 2 Function file (same as Q1 for corrected smallest factor)

#Original Function (Humpherys and Jarvis, p. 99)  
    
#Corrected Function 

def smallest_factor(n): 
    """Return the smallest prime factor of the positive integer n.""" 
    if n == 1: return 1 
    for i in range(2, int(n**.5) + 1): 
        if n % i == 0: return i 

#Month function

def month_length(month, leap_year=False): 
    """Return the number of days in the given month.""" 
    if month in {"September", "April", "June", "November"}: 
        return 30 
    elif month in {"January", "March", "May", "July", 
                       "August", "October", "December"}: 
        return 31 
    if month == "February": 
        if not leap_year: 
            return 28 
        else: 
            return 29 
    else: 
        return None
        