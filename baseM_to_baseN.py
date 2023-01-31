

import decimal_to_base_n

nums = [i for i in range(36)]
chars = [str(i) for i in range(10)] + [chr(i + 65) for i in range(26)]  # type: ignore

def base_n_to_decimal(num_str: str, base: int) -> int:
    res = 0
    n = len(num_str)
    
    base_n_hashmap = {}
    for i in range(base):
        base_n_hashmap[chars[i]] = nums[i]

    for i in range(n - 1, -1, -1):
        num_idx = n - i - 1
        res += base_n_hashmap[num_str[i]] * (base ** num_idx)
    return res


def BaseToBase(num_str: str, base_m: int, base_n: int) -> str:
    # Convert to decimal first
    decimal = base_n_to_decimal(num_str, base_m)

    # from decimal to base_n
    res = decimal_to_base_n.decimal_to_base_n(str(decimal), base_n)

    return res


if __name__ == '__main__':
    assert BaseToBase('0', 5, 2) == '0'
    assert BaseToBase('1324', 5, 2) == '11010110'
    assert BaseToBase('1324', 5, 32) == '6M'
    assert BaseToBase('1324', 16, 32) == '4P4'
    assert BaseToBase('1324', 32, 5) == '2122113'

    print('All tests passed!')





'''
import DecimalToBaseN

nums = [i for i in range(36)]
chars = [str(i) for i in range(10)] + [chr(i + 65) for i in range(26)]  # type: ignore

def base_n_to_decimal(num_str: str, base: int) -> int:
    res = 0
    n = len(num_str)
    for i in range(n - 1, -1, -1):
        num_idx = n - i - 1
        res += nums[chars.index(num_str[i])] * (base ** num_idx)
    return res

def BaseToBase(num_str: str, base_m: int, base_n: int) -> str:
    # base_mhashmap = {}
    # for i in range(base_m):
    #     base_mhashmap[chars[i]] = nums[i]

    # base2hashmap = {}
    # for i in range(base_n):
    #     base2hashmap[nums[i]] = chars[i]

    # Convert to decimal first
    decimal = base_n_to_decimal(num_str, base_m)

    # from decimal to base_n
    res = DecimalToBaseN.decimal_to_base_n(str(decimal), base_n)


    return res
'''