class ConextXWWarnings:
    def getBitList(self, val):
        l = []
        if(isinstance(val, float)):
            val = int(val)
        bin_val = bin(val)[2:]
        r_bin_val = bin_val[::-1]
        for i in range(len(r_bin_val)):
            if(r_bin_val[i] != '0'):
                l.append('bit'+str(i))
        return l
    
    def getBitmap0Warning(self, lis):
        d = {}
        l = []
        d['bit0'] = "W44:Battery Over Temperature"
        d['bit1'] = "W45:Capacitor Over Temperature"
        d['bit2'] = "W48:DC Under Voltage"
        d['bit3'] = "W49:DC Over Voltage"
        d['bit4'] = "W57:FET1 Over Temperature"
        d['bit5'] = "W58:FET2 Over Temperature"
        d['bit6'] = "W63:AC Overload"
        d['bit7'] = "W64:AC Overload"
        d['bit8'] = "W68:Transformer Over Temperature"
        d['bit9'] = "W70:Check Phase Configuration"
        d['bit10'] = "W94:Remote Power Off"
        d['bit11'] = "W95:Equalize Abort"
        d['bit12'] = "W96:Cannot Equalize"
        d['bit13'] = "W97:Battery Temperature Sensor Failure"
        d['bit14'] = "W500:Lost Network Connection"
        d['bit15'] = "W501:Non Volatile Memory Warning"
        for i in lis:
            l.append(d[i])
        return l
