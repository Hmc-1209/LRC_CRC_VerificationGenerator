def lrc(address, functional_code, data):
    val = []
    final_val = 0
    address = ('0' + address[2:]) if (len(address) % 2 != 0) else address[2:]
    functional_code = ('0' + functional_code[2:]) if (len(functional_code) % 2 != 0) else functional_code[2:]
    data = ('0' + data[2:]) if (len(data) % 2 != 0) else data[2:]

    # print(address, functional_code, data)
    for i in range(0, len(address), 2):
        val.append(str(address[i]) + str(address[i+1]))
    for i in range(0, len(functional_code), 2):
        val.append(str(functional_code[i]) + str(functional_code[i+1]))
    for i in range(0, len(data), 2):
        val.append(str(data[i]) + str(data[i+1]))

    for i in val:
        final_val += int(i, 16)

    output = (hex(256 - final_val % 256))[2:].upper()

    print("The LRC code is : ", '0' + output if len(output) == 1 else output)


def crc():
    pass


# Return the address, functional_code, data with hexadecimal no matter the input
def get_data(entering_type: int):
    address = hex(int(input("Address:").replace(" ", ""), entering_type))
    functional_code = hex(int(input("Functional code:").replace(" ", ""), entering_type))
    data = hex(int(input("Data:").replace(" ", ""), entering_type))
    print()

    return address, functional_code, data


def main():

    operating_type = input("Select verification type - 1 for LRC / 2 for CRC : ")
    entering_type = input("Select entering type - 1 for binary / 2 for hexadecimal : ")
    print()

    address, functional_code, data = (get_data(2) if entering_type == '1' else get_data(16))

    lrc(address, functional_code, data) if operating_type == '1' else crc()

    # 00000001 0
    # 00000011 0
    # 00000100000000010000000000000001 10304010001


main()
