class ConextXWFaults:
    def getBitList(self, val):
        try:
            l = []
            if(isinstance(val, float)):
                val = int(val)
            bin_val = bin(val)[2:]
            r_bin_val = bin_val[::-1]
            for i in range(len(r_bin_val)):
                if(r_bin_val[i] != '0'):
                    l.append('bit'+str(i))
            return l
        except:
            return []
    
    def getBitmap0Fault(self, lis):
        try:
            d = {}
            l = []
            d['bit0'] = "F1:AC Output UnderVolage Shutdown"
            d['bit1'] = "F2:AC Output OverVolage Shutdown"
            d['bit2'] = "F17:AC BackFeed Fault (AC1 L1)"
            d['bit3'] = "F18:AC BackFeed Fault (AC1 L2)"
            d['bit4'] = "F19:AC BackFeed Fault (AC2 L1)"
            d['bit5'] = "F20:AC Backfeed Fault (AC2 L2)"
            d['bit6'] = "F21:AC Backfeed Fault (L1L2 Weld)"
            d['bit7'] = "F22:AC Backfeed Fault( Line 1 Weld)"
            d['bit8'] = "F23:Anti-Islanding Fault (Over Freq)"
            d['bit9'] = "F24:Anti-Islanding Fault (Under Freq)"
            d['bit10'] = "F25:Anti-Islanding (Over Freq)"
            d['bit11'] = "F26:Anti-Islanding (Under Freq)"
            d['bit12'] = "F27:Anti-Islanding (Over Voltage Line 1)"
            d['bit13'] = "F28:Anti-Islanding (Over Voltage Line 2)"
            d['bit14'] = "F29:Anti-Islanding (Over Voltage)"
            d['bit15'] = "F30:Anti-Islanding (Over voltage L1L2)"
            for i in lis:
                l.append(d[i])
            return l
        except:
            return []
    
    def getBitmap1Fault(self, lis):
        try:
            d = {}
            l = []
            d['bit0'] = "F31:Anti-Islanding (Over Voltage L1 Slow)"
            d['bit1'] = "F32:Anti-Islanding (Over Voltage L2 Slow)"
            d['bit2'] = "F33:Anti-Islanding (Over Voltage L1L2 Slow)"
            d['bit3'] = "F34:Anti-Islanding (Under Voltage L1 Slow)"
            d['bit4'] = "F35:Anti-Islanding (Under Voltage L2 Slow)"
            d['bit5'] = "F36:Anti-Islanding (Under Voltage L1L2 Slow)"
            d['bit6'] = "F37:Anti-Islanding (Under Voltage L1 Fast)"
            d['bit7'] = "F38:Anti-Islanding (Under Voltage L2 Fast)"
            d['bit8'] = "F39:Anti-Islanding (Under Voltage)"
            d['bit9'] = "F40:Anti-Islanding (Under Voltage L1L2 Fast)"
            d['bit10'] = "F41:APS Under Voltage"
            d['bit11'] = "F42:APS Over Voltage"
            d['bit12'] = "F44:Battery Over Temperature"
            d['bit13'] = "F45:Capacitor Over Temperature"
            d['bit14'] = "F46:Controller Error"
            d['bit15'] = "F47:DC Under Voltage Immediate"
            for i in lis:
                l.append(d[i])
            return l
        except:
            return []
    def getBitmap2Fault(self, lis):
        try:
            d = {}
            l = []
            d['bit0'] = "F48:DC Under-Voltage Shutdown"
            d['bit1'] = "F49:DC Over-Voltage Shutdown"
            d['bit2'] = "F51:EEPROM Error"
            d['bit3'] = "F52:EEPROM Error (Cal Fail)"
            d['bit4'] = "F53:EEPROM Error (Config Fail)"
            d['bit5'] = "F54:EEPROM Error (Default Fail)"
            d['bit6'] = "F55:EEPROM Error (Log Fail)"
            d['bit7'] = "F56:EEPROM Error (Strings Fail)"
            d['bit8'] = "F57:FET1 Over-Temperature Shutdown"
            d['bit9'] = "F58:FET2 Over-Temperature Shutdown"
            d['bit10'] = "F59:Configuration Copy Error"
            d['bit11'] = "F60:Invalid Fault"
            d['bit12'] = "F61:Invalid Warning"
            d['bit13'] = "F62:Invalid Interrupt"
            d['bit14'] = "F63:AC Overload (Primary)"
            d['bit15'] = "F64:AC Overload (Secondary 1s)"
            for i in lis:
                l.append(d[i])
            return l
        except:
            return []
    def getBitmap3Fault(self, lis):
        try:
            d = {}
            l = []
            d['bit0'] = "F65:AC Overload (2s)"
            d['bit1'] = "F66:System Configuration Error"
            d['bit2'] = "F67:Watchdog Reset"
            d['bit3'] = "F68:Transformer Over-Temperature"
            d['bit4'] = "F69:Synchronization Signal Fault"
            d['bit5'] = "F70:Three Phase Configuration Fault"
            for i in lis:
                l.append(d[i])
            return l
        except:
            return []
