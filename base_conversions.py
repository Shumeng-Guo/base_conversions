'''
1. from Base_N to Decimal
2. from Decimal to Binary
3. from Decimal to Hex
4. from Decimal to Base_N
5. from Base_M to Base_N
'''


from collections import deque

nums = [i for i in range(36)]
chars = [str(i) for i in range(10)] + [chr(i + ord('A')) for i in range(26)]


# from Base N to Decimal
def base_n_to_decimal(num_str: str, base: int) -> int:   # type: ignore
    res = 0
    n = len(num_str)
    
    base_n_hashmap = {}
    for i in range(base):
        base_n_hashmap[chars[i]] = nums[i]

    for i in range(n - 1, -1, -1):
        num_idx = n - i - 1
        res += base_n_hashmap[num_str[i]] * (base ** num_idx)
    return res


##################################################################################


# from Decimal to Binary
def decimal_to_binary(decimal_str: str) -> str:
    res = []
    dq = deque()

    decimal = int(decimal_str)
    dec_quotient = decimal

    if dec_quotient == 0:
        return '0'

    while dec_quotient > 0: 
        bin_ones = dec_quotient % 2
        dq.appendleft(str(bin_ones))
        
        dec_quotient = dec_quotient // 2

    res = ''.join(list(dq))
    return res  # type: ignore


##################################################################################


# from Decimal to Hex
def decimal_to_hex(decimal_str: str) -> str: # type: ignore
    res = []
    dq = deque()

    hex_hashmap = {}
    for i in range(16):
        hex_hashmap[nums[i]] = chars[i]

    decimal = int(decimal_str)
    dec_quotient = decimal

    if dec_quotient == 0:
        return '0'

    while dec_quotient > 0: 
        hex_ones = dec_quotient % 16
        dq.appendleft(hex_hashmap[hex_ones])       
        dec_quotient = dec_quotient // 16
    

    res = ''.join(list(dq))

    return res


##################################################################################


# from Decimal to Base N
def decimal_to_base_n(decimal_str: str, base: int) -> str:
    res = []
    dq = deque()

    base_n_hashmap = {}
    for i in range(base):
        base_n_hashmap[nums[i]] = chars[i]

    decimal = int(decimal_str)
    dec_quotient = decimal

    if dec_quotient == 0:
        return '0'

    while dec_quotient > 0: 
        hex_ones = dec_quotient % base
        dq.appendleft(base_n_hashmap[hex_ones])       
        dec_quotient = dec_quotient // base

    
    res = ''.join(list(dq))
    return res


##################################################################################


def base_to_base(num_str: str, base_m: int, base_n: int) -> str:
    # Convert to decimal first
    decimal = base_n_to_decimal(num_str, base_m)

    # from decimal to base_n
    res = decimal_to_base_n(str(decimal), base_n)

    return res





if __name__ == '__main__':

    assert decimal_to_binary('1') == '1'
    assert decimal_to_binary('2') == '10'
    assert decimal_to_binary('18') == '10010'


    assert decimal_to_hex('16') == '10'
    assert decimal_to_hex('1787') == '6FB'

    assert decimal_to_base_n('0', 8) == '0'
    assert decimal_to_base_n('214', 5) == '1324'
    assert decimal_to_base_n('214', 32) == '6M'

    assert base_to_base('0', 5, 2) == '0'
    assert base_to_base('1324', 5, 2) == '11010110'
    assert base_to_base('1324', 5, 32) == '6M'
    assert base_to_base('1324', 16, 32) == '4P4'
    assert base_to_base('1324', 32, 5) == '2122113'

    print('All tests passed!')
