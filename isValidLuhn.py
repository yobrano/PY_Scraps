test_str = "17893729974"

def isValidLuhn(test_str):
    sample_id, validator = test_str[:-1], int(test_str[-1])
    id_digits = [int(digit) for digit in sample_id]
    is_even = len(id_digits) % 2

    # starting from the right most value double the digits but do so while alternating.
    # sum the digits in the new value (add both digits after multiplying the original by two) 
    double_alternates = []
    for idx, digit  in enumerate(id_digits):
        # if the sample_id length is even then skip first and all odd-indexed values 
        if(is_even != idx % 2):
            digit = sum([ int(i) for i in str(digit * 2)])
            double_alternates.append(digit)
        else:
            double_alternates.append(digit)

    check_value = 10 - sum(double_alternates) % 10 
    return check_value == validator