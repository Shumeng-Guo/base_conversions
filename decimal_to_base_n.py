
from collections import deque

nums = [i for i in range(36)]
chars = [str(i) for i in range(10)] + [chr(i + ord('A')) for i in range(26)]  # type: ignore


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


if __name__ == '__main__':
    assert decimal_to_base_n('0', 8) == '0'
    assert decimal_to_base_n('214', 5) == '1324'
    assert decimal_to_base_n('214', 32) == '6M'

    print('All tests passed!')
