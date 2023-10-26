def is_valid_luhn(test_str):
    sample_id, validator = test_str[:-1], int(test_str[-1])
    id_digits = [int(digit) for digit in sample_id]
    is_even = len(id_digits) % 2

    # starting from the right most value double the digits but do so while alternating.
    # sum the digits in the new value (add both digits after multiplying the original by two) 
    # for the test to be valid the last digit should be equal to ... 
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


if __name__ == "__main__":
    test_str = "79927398713"
    is_valid = is_valid_luhn(test_str)
    print("Lenght: ", len(test_str))
    print(f"The code \"{test_str}\" {'passes' if(is_valid)else('does not pass')} the Luhn test.")