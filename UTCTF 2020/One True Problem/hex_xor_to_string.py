

hex2 = input('Give me hex string: ')
pos = int(input('Give me the index of the letter to change: '))
while True:
    str1 = input('Give me a string: ')
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWYZ0123456789 '

    for c in chars:
        str1 = str1[:pos] + c + str1[pos+1:]
        
        hex1 = str1.encode().hex()
        
        int1 = int(hex1,16)
        int2 = int(hex2,16)
        
        xor = int1^int2
        
        str3 = bytearray.fromhex(hex(xor)[2:]).decode()
        print(str1, ':', str3)

    pos += 1
