from utils.read_modbus_tcp import ReadModbusTCP
import time

class ConextXW(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self.r = ReadModbusTCP(host='172.16.118.22', port='502', auto_open=True)
        self.r.open()
        self.r.clearGlobalDict() #very_important
    
    def portCheck(self):
        while True:
            time.sleep(5)
            if not self.r.is_open():
                self.r.open()
            else:
                break
	
    




    #################  HW SERIAL NUMBER  #########################################
    def getHWSerialNumber(self):
        self.r.grab_str_data(10, 0x002B, self.device_id)
        return self.r.getGlobalDict().get(str(0x002B))




    #################  MODBUS ADDRESS  #########################################
    def getModbusAddress(self):
        self.r.grab_uint_data(1, 0x0028, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x0028))
    



    #################  FAULTS  #########################################
    def getActiveFaultsFlag(self):
        #0 - No Faults, 1 - Active Faults
        self.r.grab_uint_data(1, 0x004B, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x004B))

    def getBitmap0Fault(self):
        self.r.grab_uint_data(1, 0x0042, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x0042))
    
    def getBitmap1Fault(self):
        self.r.grab_uint_data(1, 0x0043, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x0043))
    
    def getBitmap2Fault(self):
        self.r.grab_uint_data(1, 0x0044, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x0044))
    
    def getBitmap3Fault(self):
        self.r.grab_uint_data(1, 0x0045, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x0045))

    




    #################  WARNINGS  #########################################
    def getActiveWarningsFlag(self):
        #0 - No Warnings, 1 - Active Warnings
        self.r.grab_uint_data(1, 0x004C, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x004C))

    def getBitmap0Warning(self):
        self.r.grab_uint_data(1, 0x0046, self.device_id, 1.0, 0.0, '')
        return self.r.getGlobalDict().get(str(0x0046))
    




    #################  BATTERY  #########################################
    def getBatteryVoltage(self):
        self.r.grab_uint_data(2, 0x0050, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x0050))
    
    def getBatteryCurrent(self):
        self.r.grab_sint_data(2, 0x0052, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0052))
    
    def getBatteryPower(self):
        self.r.grab_sint_data(2, 0x0054, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x0054))
    
    def getBatteryTemperature(self):
        self.r.grab_uint_data(1, 0x0056, self.device_id, 0.01, -273.0, 'deg C')
        return self.r.getGlobalDict().get(str(0x0056))
    
    def getInvertDCCurrent(self):
        self.r.grab_uint_data(2, 0x0058, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0058))
    
    def getInvertDCPower(self):
        self.r.grab_uint_data(2, 0x005A, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x005A))
    
    def getChargeDCCurrent(self):
        self.r.grab_uint_data(2, 0x005C, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x005C))
    
    def getChargeDCPower(self):
        self.r.grab_uint_data(2, 0x005E, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x005E))
    
    def getChargeDCPowerPercentage(self):
        self.r.grab_uint_data(1, 0x0060, self.device_id, 1.0, 0.0, '%')
        return self.r.getGlobalDict().get(str(0x0060))
    
    def getEnergyFromBatteryHour(self):
        self.r.grab_uint_data(2, 0x00D0, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00D0))
    
    def getEnergyFromBatteryToday(self):
        self.r.grab_uint_data(2, 0x00D4, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00D4))
    
    def getEnergyFromBatteryWeek(self):
        self.r.grab_uint_data(2, 0x00D8, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00D8))
    
    def getEnergyFromBatteryMonth(self):
        self.r.grab_uint_data(2, 0x00DC, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00DC))
    
    def getEnergyFromBatteryYear(self):
        self.r.grab_uint_data(2, 0x00E0, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00E0))
    
    def getEnergyFromBatteryLifeTime(self):
        self.r.grab_uint_data(2, 0x00E4, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00E4))
    
    def getEnergyToBatteryHour(self):
        self.r.grab_uint_data(2, 0x00E8, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00E8))
    
    def getEnergyToBatteryToday(self):
        self.r.grab_uint_data(2, 0x00EC, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00EC))
    
    def getEnergyToBatteryWeek(self):
        self.r.grab_uint_data(2, 0x00F0, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00F0))
    
    def getEnergyToBatteryMonth(self):
        self.r.grab_uint_data(2, 0x00F4, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00F4))
    
    def getEnergyToBatteryYear(self):
        self.r.grab_uint_data(2, 0x00F8, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00F8))
    
    def getEnergyToBatteryLifeTime(self):
        self.r.grab_uint_data(2, 0x00FC, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x00FC))
    




    #################  GRID  #########################################
    def getGridACFrequency(self):
        self.r.grab_uint_data(1, 0x0061, self.device_id, 0.01, 0.0, 'Hz')
        return self.r.getGlobalDict().get(str(0x0061))
    
    def getGridACVoltage(self):
        self.r.grab_uint_data(2, 0x0062, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x0062))
    
    def getGridACCurrent(self):
        self.r.grab_sint_data(2, 0x0064, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0064))
    
    def getGridACPower(self):
        self.r.grab_sint_data(2, 0x0066, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x0066))
    
    def getGridACInputApparentPower(self):
        self.r.grab_uint_data(2, 0x0068, self.device_id, 1.0, 0.0, 'VA')
        return self.r.getGlobalDict().get(str(0x0068))

    def getGridACInputCurrent(self):
        self.r.grab_uint_data(2, 0x006A, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x006A))
    
    def getGridACInputPower(self):
        self.r.grab_uint_data(2, 0x006C, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x006C))
    
    def getGridACL1Voltage(self):
        self.r.grab_uint_data(2, 0x006E, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x006E))
    
    def getGridACL2Current(self):
        self.r.grab_sint_data(2, 0x0070, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0070))
    
    def getGridACL2Voltage(self):
        self.r.grab_uint_data(2, 0x0072, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x0072))
    
    def getGridACL1Current(self):
        self.r.grab_sint_data(2, 0x0074, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0074))
    
    def getGridOutputVoltage(self):
        self.r.grab_uint_data(2, 0x007E, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x007E))
    
    def getGridOutputCurrent(self):
        self.r.grab_uint_data(2, 0x0080, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0080))
    
    def getGridOutputFrequency(self):
        self.r.grab_uint_data(1, 0x0082, self.device_id, 0.01, 0.0, 'Hz')
        return self.r.getGlobalDict().get(str(0x0082))
    
    def getGridOutputPower(self):
        self.r.grab_uint_data(2, 0x0084, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x0084))
    
    def getGridOutputApparentPower(self):
        self.r.grab_uint_data(2, 0x008A, self.device_id, 1.0, 0.0, 'VA')
        return self.r.getGlobalDict().get(str(0x008A))

    def getGridInputEnergyHour(self):
        self.r.grab_uint_data(2, 0x0100, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0100))
    
    def getGridInputEnergyToday(self):
        self.r.grab_uint_data(2, 0x0104, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0104))
    
    def getGridInputEnergyWeek(self):
        self.r.grab_uint_data(2, 0x0108, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0108))
    
    def getGridInputEnergyMonth(self):
        self.r.grab_uint_data(2, 0x010C, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x010C))
    
    def getGridInputEnergyYear(self):
        self.r.grab_uint_data(2, 0x0110, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0110))
    
    def getGridInputEnergyLifeTime(self):
        self.r.grab_uint_data(2, 0x0114, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0114))
    
    def getGridOutputEnergyHour(self):
        self.r.grab_uint_data(2, 0x0118, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0118))
    
    def getGridOutputEnergyToday(self):
        self.r.grab_uint_data(2, 0x011C, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x011C))
    
    def getGridOutputEnergyWeek(self):
        self.r.grab_uint_data(2, 0x0120, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0120))
    
    def getGridOutputEnergyMonth(self):
        self.r.grab_uint_data(2, 0x0124, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0124))
    
    def getGridOutputEnergyYear(self):
        self.r.grab_uint_data(2, 0x0128, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0128))
    
    def getGridOutputEnergyLifeTime(self):
        self.r.grab_uint_data(2, 0x012C, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x012C))
    



    #################  LOAD  #########################################
    def getLoadACVoltage(self):
        self.r.grab_uint_data(2, 0x008C, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x008C))
    
    def getLoadACL1Voltage(self):
        self.r.grab_uint_data(2, 0x008E, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x008E))
    
    def getLoadACL2Voltage(self):
        self.r.grab_uint_data(2, 0x0090, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x0090))
    
    def getLoadACL1Current(self):
        self.r.grab_uint_data(2, 0x0092, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0092))
    
    def getLoadACL2Current(self):
        self.r.grab_uint_data(2, 0x0094, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0094))
    
    def getLoadACCurrent(self):
        self.r.grab_uint_data(2, 0x0096, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x0096))
    
    def getLoadACFrequency(self):
        self.r.grab_uint_data(1, 0x0098, self.device_id, 0.01, 0.0, 'Hz')
        return self.r.getGlobalDict().get(str(0x0098))
    
    def getLoadACPower(self):
        self.r.grab_uint_data(2, 0x009A, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x009A))
    
    def getLoadACApparentPower(self):
        self.r.grab_uint_data(2, 0x00A0, self.device_id, 1.0, 0.0, 'VA')
        return self.r.getGlobalDict().get(str(0x00A0))
    
    def getLoadOutputEnergyHour(self):
        self.r.grab_uint_data(2, 0x0130, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0130))
    
    def getLoadOutputEnergyToday(self):
        self.r.grab_uint_data(2, 0x0134, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0134))
    
    def getLoadOutputEnergyWeek(self):
        self.r.grab_uint_data(2, 0x0138, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0138))
    
    def getLoadOutputEnergyMonth(self):
        self.r.grab_uint_data(2, 0x013C, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x013C))
    
    def getLoadOutputEnergyYear(self):
        self.r.grab_uint_data(2, 0x0140, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0140))
    
    def getLoadOutputEnergyLifeTime(self):
        self.r.grab_uint_data(2, 0x0144, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0144))
    



    #################  GEN  #########################################
    def getGenACVoltage(self):
        self.r.grab_uint_data(2, 0x00A2, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x00A2))
    
    def getGenACCurrent(self):
        self.r.grab_uint_data(2, 0x00A4, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x00A4))
    
    def getGenACFrequency(self):
        self.r.grab_uint_data(1, 0x00A6, self.device_id, 0.01, 0.0, 'Hz')
        return self.r.getGlobalDict().get(str(0x00A6))
    
    def getGenACPower(self):
        self.r.grab_uint_data(2, 0x00AC, self.device_id, 1.0, 0.0, 'W')
        return self.r.getGlobalDict().get(str(0x00AC))
    
    def getGenACL1Voltage(self):
        self.r.grab_uint_data(2, 0x00B2, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x00B2))
    
    def getGenACL1Current(self):
        self.r.grab_uint_data(2, 0x00B4, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x00B4))
    
    def getGenACL2Voltage(self):
        self.r.grab_uint_data(2, 0x00B6, self.device_id, 0.001, 0.0, 'V')
        return self.r.getGlobalDict().get(str(0x00B6))
    
    def getGenACL2Current(self):
        self.r.grab_uint_data(2, 0x00B8, self.device_id, 0.001, 0.0, 'A')
        return self.r.getGlobalDict().get(str(0x00B8))
    
    def getGenACApparentPower(self):
        self.r.grab_uint_data(2, 0x00BA, self.device_id, 1.0, 0.0, 'VA')
        return self.r.getGlobalDict().get(str(0x00BA))
    
    def getGenInputEnergyHour(self):
        self.r.grab_uint_data(2, 0x0148, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0148))
    
    def getGenInputEnergyToday(self):
        self.r.grab_uint_data(2, 0x014C, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x014C))
    
    def getGenInputEnergyWeek(self):
        self.r.grab_uint_data(2, 0x0150, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0150))
    
    def getGenInputEnergyMonth(self):
        self.r.grab_uint_data(2, 0x0154, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0154))
    
    def getGenInputEnergyYear(self):
        self.r.grab_uint_data(2, 0x0158, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x0158))
    
    def getGenInputEnergyLifeTime(self):
        self.r.grab_uint_data(2, 0x015C, self.device_id, 0.001, 0.0, 'kWh')
        return self.r.getGlobalDict().get(str(0x015C))
    


