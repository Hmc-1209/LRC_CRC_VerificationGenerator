def lrc(address, functional_code, data):
    # Setting empty list for separating each two hexa chars
    val = []
    # Final value uses for adding all pairs up
    final_val = 0

    # For each data, check if it needs to add '0' in the beginning for making pairs
    address = ('0' + address[2:]) if (len(address) % 2 != 0) else address[2:]
    functional_code = ('0' + functional_code[2:]) if (len(functional_code) % 2 != 0) else functional_code[2:]
    data = ('0' + data[2:]) if (len(data) % 2 != 0) else data[2:]

    # Separate to pairs
    for data_type in [address, functional_code, data]:
        for i in range(0, len(data_type), 2):
            val.append(str(data_type[i]) + str(data_type[i+1]))

    # Summing up
    for i in val:
        final_val += int(i, 16)
    # Make it for uppercase for beautify
    output = (hex(256 - final_val % 256))[2:].upper()
    print("The LRC code is : ", '0' + output if len(output) == 1 else output)


def crc(address, functional_code, data_in, entering_type):
    crc_register = 0xFFFF   # Original CRC code

    # Assembling data
    bin_data = ""
    if entering_type == '2':
        for data_type in [address, functional_code, data_in]:
            if data_type != '0':
                bin_data += data_type
    else:
        for data_type in [address, functional_code, data_in]:
            if data_type != '0':
                hex_str = hex(int(data_type, 2)).zfill((len(data_type) / 4).__floor__())[2:]
                pad = (len(data_type) / 4).__ceil__() - len(hex_str)
                bin_data += '0' * pad + hex_str

    # Automatic padding for convert to two bytes each pair
    if len(bin_data) % 2 != 0:
        bin_data = '0' + bin_data

    bin_data = bytes.fromhex(bin_data)

    # Shifting and XORing
    for byte in bin_data:
        crc_register ^= byte
        for _ in range(8):
            if crc_register & 0x0001:
                crc_register = (crc_register >> 1) ^ 0xA001
            else:
                crc_register >>= 1

    print("The CRC code is :", crc_register.to_bytes(2, "little").hex().upper())


# Return the address, functional_code, data with hexadecimal no matter the input
def get_data(entering_type: int, operating_type):
    address = input("Address:").replace(" ", "")
    functional_code = input("Functional code:").replace(" ", "")
    data = input("Data:").replace(" ", "")
    print()

    if operating_type == '1':
        return hex(int(address, entering_type)), hex(int(functional_code, entering_type)), hex(int(data, entering_type))
    else:
        return address, functional_code, data


def main():

    operating_type = input("Select verification type - 1 for LRC / 2 for CRC : ")
    entering_type = input("Select entering type - 1 for binary / 2 for hexadecimal : ")
    print()

    address, functional_code, data = (get_data(2, operating_type) if entering_type == '1' else get_data(16, operating_type))

    lrc(address, functional_code, data) if operating_type == '1' else crc(address, functional_code, data, entering_type)

    # 00000001 0
    # 00000011 0
    # 00000100000000010000000000000001 10304010001


main()
