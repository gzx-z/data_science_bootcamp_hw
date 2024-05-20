# define Imem Dmem and Registers

import os

MemSize = 1000


class ins_mem(object):
    # read instruction
    def __init__(self, name, io_dir):
        self.id = name

        with open(ioDir + os.sep + "imem.txt") as im:
            self.imem = [data.replace("\n", "") for data in im.readlines()]

    def read_inst(self, read_address):
        # read instruction memory
        # return 32 bit hex val
        inst = int("".join(self.i_mem[read_address:read_address + 4]), 2)
        # change into decimal number
        return format(inst, '#010x')

    def read_instr(self, read_address: int) -> str:
        # read instruction memory
        # return 32 bit str binary instruction
        return "".join(self.imem[read_address:read_address + 4])


class data_mem(object):
    def __init__(self, name, io_dir):
        self.id = name
        self.io_dir = io_dir
        with open(io_dir + os.sep + "dmem.txt") as dm:
            self.dmem = [data.replace("\n", "") for data in dm.readlines()]
        # fill in the empty memory with 0s
        self.dmem = self.dmem + (['00000000'] * (mem_size - len(self.dmem)))

    def read_data_mem(self, read_address):
        # read data memory
        # return 32 bit hex val 8
        data32 = int("".join(self.dmem[read_address: read_address + 4]), 2)  # change into decimal number
        return format(data32, '#010x')  # '0x'+8 bit hex

    def write_data_mem(self, address, write_data):
        # write data into byte addressable memory
        mask8 = int('0b11111111', 2)  # 8-bit mask
        data8_arr = []

        for j in range(4):
            data8_arr.append(write_data & mask8)
            write_data = write_data >> 8

        for i in range(4):
            # most significant bit(last element in data8_arr) in smallest address
            self.dmem[address + i] = format(data8_arr.pop(), '08b')

    # five stage func
    def read_data_mem(self, read_addr: str) -> str:
        # read data memory
        # return 32 bit hex val
        read_addr_int = bin2int(read_addr)
        return "".join(self.DMem[read_addr_int: read_addr_int + 4])

    def write_data_mem(self, addr: str, write_data: str):
        # write data into byte addressable memory
        addr_int = bin2int(addr)
        for i in range(4):
            self.dmem[addr_int + i] = write_data[8 * i: 8 * (i + 1)]

    # output file of Dmem  SS_DMEMResult.txt              
    def outpur_data_mem(self):
        resPath = self.ioDir + os.sep + self.id + "_DMEMResult.txt"
        with open(res_path, "w") as rp:
            rp.writelines([str(data) + "\n" for data in self.dmem])


class register_file(object):
    def __init__(self, io_dir):
        self.outputFile = io_dir + "RFResult.txt"
        self.Registers = [0x0 for i in range(32)]  # 32 registers for single cycle
        self.registers = [int2bin(0) for _ in range(32)]  # five stage

    def read_rf(self, reg_addr):  # read register
        return self.registers[reg_addr]

    def write_rf(self, reg_addr, wrt_reg_data):  # write into registers
        if reg_addr != 0:
            self.registers[reg_addr] = wrt_reg_data & ((1 << 32) - 1)  # and 32 bits 1 mask

    # output file of registers  SS_RFResult.txt
    def output_rf(self, cycle):
        op = ["State of RF after executing cycle:  " + str(cycle) + "\n"]  # "-"*70+"\n",  dividing line
        op.extend([format(val, '032b') + "\n" for val in self.registers])
        if cycle == 0:
            perm = "w"
        else:
            perm = "a"
        with open(self.output_file, perm) as file:
            file.writelines(op)

    # five stage
    def read_rf(self, reg_addr: str) -> str:
        # Fill in
        return self.registers[bin_to_int(reg_addr)]

    def write_rf(self, reg_addr: str, wrt_reg_data: str):
        # Fill in
        if reg_addr == "00000":
            return
        self.registers[bin_to_int(reg_addr)] = wrt_reg_data

    def output_rf(self, cycle):
        op = ["State of RF after executing cycle:" + str(cycle) + "\n"]
        op.extend([f"{val}" + "\n" for val in self.registers])
        if cycle == 0:
            perm = "w"
        else:
            perm = "a"
        with open(self.output_file, perm) as file:
            file.writelines(op)


def int_to_bin(x: int, n_bits: int = 32) -> str:
    bin_x = bin(x & (2 ** n_bits - 1))[2:]
    return "0" * (n_bits - len(bin_x)) + bin_x


def bin_to_int(x: str, sign_ext: bool = False) -> int:
    x = str(x)
    if sign_ext and x[0] == "1":
        return -(-int(x, 2) & (2 ** len(x) - 1))
    return int(x, 2)
