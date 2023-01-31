
from collections import deque

nums = [i for i in range(36)]
chars = [str(i) for i in range(10)] + [chr(i + ord('A')) for i in range(26)]

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



if __name__ == '__main__':
    assert decimal_to_hex('0') == '0'
    assert decimal_to_hex('1') == '1'
    assert decimal_to_hex('16') == '10'
    assert decimal_to_hex('1787') == '6FB'
    assert decimal_to_hex('18888') == '49C8'

    print('All tests passed!')
