from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import binascii


class ReadModbusTCP(ModbusClient):
    value_dict = {}
        
    def decimal_to_hexadecimal(self, dec):
        decimal = int(dec)
        if(hex(decimal)[0] == '-'):
            return '-' + hex(decimal)[3:]
        else:
            return hex(decimal)[2:]

    def hexadecimal_to_string(self, _hex):
        return binascii.unhexlify(_hex)

    def hexadecimal_to_int(self, _hex):
        return int(str(_hex), 16)

    def convertDataToUnit(self, data, scale, offset):
        return (data * scale) + offset

    #str16, str32
    def grab_str_data(self, n_reg, hex_addr, modbus_addr):
        addr = int(hex_addr)
        str_ = ""
        if self.is_open():
            self.unit_id(modbus_addr)
            regs = self.read_holding_registers(addr, n_reg)
            #print regs
            if regs:
                for i in regs:
                    if(i != 0):
                        hex_val = self.decimal_to_hexadecimal(int(i))
                        str_val = self.hexadecimal_to_string(hex_val)
                        str_ += str_val
                #print ("Read value @ address " + str(hex(addr)) + " is " + str_)
                self.value_dict[str(hex_addr)] = str_

    #uint16, uint32
    def grab_uint_data(self, n_reg, hex_addr, modbus_addr, scale, offset, unit_symbol):
        ans = ""	
        addr = int(hex_addr)
        str_ = ""
        s_val = ""
        if self.is_open():
            self.unit_id(modbus_addr)
            regs = self.read_holding_registers(addr, n_reg)
            if regs:
                #print("reg ad #0 to 9: "+str(regs))
                if n_reg == 1: #in the case of uint16
                    for i in regs:
                        if(i != 0 and i != 65535 and i != 4294967295): 
                            hex_val = self.decimal_to_hexadecimal(int(i))
                            s_val += hex_val
                    if len(s_val) == 0:
                        str_ = "0"
                        #print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                        #print ("Converted data is " + str(str_) + " " + unit_symbol)
                        ans = str(str_)
                        self.value_dict[str(hex_addr)] = ans
                    else:
                        str_val = str(self.hexadecimal_to_int(s_val))
                        str_ += str_val
                        #print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                        #print ("Converted data is " + str(self.convertDataToUnit(int(str_), scale, offset)) + " " + unit_symbol)
                        ans = str(self.convertDataToUnit(int(str_), scale, offset))
                        self.value_dict[str(hex_addr)] = ans

                if n_reg == 2: #in the case of uint32
                    for i in regs:
                        if(i != 0 and i != 65535 and i != 4294967295): 
                            hex_val = self.decimal_to_hexadecimal(int(i))
                            s_val += hex_val
                    if len(s_val) == 0:
                        str_ = "0"
                        #print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                        #print ("Converted data is " + str(str_) + " " + unit_symbol)
                        ans = str(str_)
                        self.value_dict[str(hex_addr)] = ans
                    else:
                        str_val = str(self.hexadecimal_to_int(s_val))
                        str_ += str_val
                        #print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                        #print ("Converted data is " + str(self.convertDataToUnit(int(str_), scale, offset)) + " " + unit_symbol)
                        ans = str(self.convertDataToUnit(int(str_), scale, offset))
                        self.value_dict[str(hex_addr)] = ans
        
    #sint32
    def grab_sint_data(self, n_reg, hex_addr, modbus_addr, scale, offset, unit_symbol):
        ans = ""	
        addr = int(hex_addr)
        str_ = ""
        s_val = ""
        if self.is_open():
            self.unit_id(modbus_addr)
            regs = self.read_holding_registers(addr, n_reg)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
                for i in regs:
                    if(i != 0 and i != 65535 and i != 4294967295):
                        hex_val = self.decimal_to_hexadecimal(int(i))
                        s_val += hex_val
                if len(s_val) == 0:
                    str_ = "0"
                    print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                    print ("Converted data is " + str(str_) + " " + unit_symbol)
                    ans = str(str_)
                    self.value_dict[str(hex_addr)] = ans
                else:
                    str_val = str(self.hexadecimal_to_int(s_val))
                    str_ += str_val
                    if (int(str_) > 2147483647):
                        r = '-' + str_
                        str_ = str(int(r) + 2**32)
                        print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                        print ("Converted data is " + str(self.convertDataToUnit(int(str_), scale, offset)) + " " + unit_symbol)
                        ans = str(self.convertDataToUnit(int(str_), scale, offset))
                        self.value_dict[str(hex_addr)] = ans
                    else:
                        print ("Read value @ address " + str(hex(addr)) + " is " + str(str_))
                        print ("Converted data is " + str(self.convertDataToUnit(int(str_), scale, offset)) + " " + unit_symbol)
                        ans = str(self.convertDataToUnit(int(str_), scale, offset))
                        self.value_dict[str(hex_addr)] = ans
    
    def grab_float_data(self, hex_addr, number, device_addr, x="input"):
        if self.is_open():
            self.unit_id(device_addr)
            if x == "input":
                reg_l = self.read_input_registers(int(hex_addr), number * 2)
                if reg_l:
                    self.value_dict[str(hex_addr)]  = str([utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)][0])
                else:
                    self.value_dict[str(hex_addr)] = "0.0"
            elif x == "holding":
                reg_l = self.read_holding_registers(int(hex_addr), number * 2)
                if reg_l:
                    self.value_dict[str(hex_addr)]  = str([utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)][0])
                else:
                    self.value_dict[str(hex_addr)] = "0.0"

    def getGlobalDict(self):
        return self.value_dict

    def clearGlobalDict(self):
        self.value_dict.clear()