from invalid_addend_exception import InvalidAddnedException


def add(numbers):
    result = 0
    is_not_negative = ensure_no_negatives(numbers)

    if numbers == "":
        pass
    elif has_no_separators(numbers):
        result = parse_single_number(is_not_negative, numbers)
    elif uses_custom_separator(numbers):
        result = parse_custom_separator(is_not_negative, numbers)
    else:
        result = parse_standard_separators(is_not_negative, numbers)
    return result


def parse_single_number(is_not_negative, numbers):
    if is_not_negative:
        return int(numbers)

    identify_negatives([numbers])


def parse_standard_separators(is_not_negative, numbers):
    comma_nums = numbers.split(",")
    combined_nums = split_array_elements(comma_nums, "\n")
    result = prepare_final_numbers(combined_nums, is_not_negative)
    return result


def parse_custom_separator(is_not_negative, numbers):
    custom_array = numbers.split("\n")
    custom_separator = custom_array[0][2:3]
    custom_nums = custom_array[1].split(custom_separator)
    result = prepare_final_numbers(custom_nums, is_not_negative)
    return result


def ensure_no_negatives(numbers):
    return numbers.find("-") == -1


def uses_custom_separator(numbers):
    return numbers.find("//") == 0


def split_array_elements(num_array, separator):
    return_array = []
    for num in num_array:
        if num.find(separator):
            temp_array = num.split(separator)
            for temp in temp_array:
                return_array.append(temp)
        else:
            return_array.append(num)
    return return_array


def prepare_final_numbers(num_array, is_not_negative):
    if is_not_negative:
        return add_nums_in_array(num_array)
    else:
        identify_negatives(num_array)


def identify_negatives(num_array):
    invalid_nums = []
    for num in num_array:
        if num.startswith("-"):
            invalid_nums.append(num)

    raise InvalidAddnedException(invalid_nums)


def add_nums_in_array(num_array):
    result = 0
    for num in num_array:
        result += int(num)

    return result


def has_no_separators(numbers):
    return numbers.find(",") == -1 & numbers.find("\n") == -1
