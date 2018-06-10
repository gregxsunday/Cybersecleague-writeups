with open('led.txt') as file:
    blinks = file.read()
    start = blinks.find('1' * 45)
    blinks = blinks[start:]
    start = blinks.find('0')
    blinks = blinks[start:]

    bits = blinks.replace('111', 'one').replace('000', 'zero').replace('11', 'one').replace('00', 'zero'). \
        replace('1','').replace('0','').replace('one', '1').replace('zero', '0')

    with open('bits.txt', 'w') as outfile:
        outfile.write(bits)
