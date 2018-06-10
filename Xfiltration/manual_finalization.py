with open('bits.txt') as infile:
    bits = infile.read().replace('\n', '')
    res = ''
    for byte in [bits[i:i + 9] for i in range(0, len(bits), 9)]:
        print('byte: %s = %d, sychro: %s' % (byte[:8], int(byte[:8], 2), byte[8:]))
        res += chr(int(byte[:8], 2))


with open('bits.txt', 'w') as outfile:
    outfile.write('\n'.join(bits[i:i + 9] for i in range(0, len(bits), 9)))

print(res)