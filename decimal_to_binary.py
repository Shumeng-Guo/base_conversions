
from collections import deque

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
        # a deque is a double-ended queue, so we can insert on either side w/ appendleft() or append() in O(1) time
        
        dec_quotient = dec_quotient // 2
    

    res = ''.join(list(dq))
    return res  # type: ignore


if __name__ == '__main__':
    assert decimal_to_binary('0') == '0'
    assert decimal_to_binary('1') == '1'
    assert decimal_to_binary('2') == '10'

    assert decimal_to_binary('18') == '10010'
    assert decimal_to_binary('256') == '100000000'

    print('All tests passed!')