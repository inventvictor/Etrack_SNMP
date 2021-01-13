from pysnmp.entity import engine, config
from pysnmp import debug
from pysnmp.entity.rfc3413 import cmdrsp, context, ntforg
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder
from pysnmp.proto import rfc1902
from conext_xw.conext_xw_api import ConextXW
from conext_xw.conext_xw_faults import ConextXWFaults
from conext_xw.conext_xw_warnings import ConextXWWarnings

import threading
import collections
import time

#can be useful
#debug.setLogger(debug.Debug('all'))

MibObject = collections.namedtuple('MibObject', ['mibName',
                                   'objectType', 'valueFunc'])

class ConextXWSNMPDataCreator(ConextXW):
    def __init__(self, **kwargs):
        super(ConextXWSNMPDataCreator, self).__init__(kwargs.get("addr"))
        conext_xw_device_fault = ConextXWFaults()
        conext_xw_device_warn = ConextXWWarnings()
        self.portCheck()

class Mib(object):
    """Stores the data we want to serve. 
    """

    def __init__(self):
        self._lock = threading.RLock()
        self._test_count = 0
        self._etg_battery_voltage = ""
        self._etg_battery_current = ""
        self._etg_battery_power = ""
        self._etg_battery_temperature = ""
        self._etg_battery_invert_current = ""
        self._etg_battery_invert_power = ""
        self._etg_battery_charge_current = ""
        self._etg_battery_charge_power = ""
        self._etg_charge_power_percentage = ""
        self._etg_energy_from_battery_hour = ""
        self._etg_energy_from_battery_day = ""
        self._etg_energy_from_battery_week = ""
        self._etg_energy_to_battery_hour = ""
        self._etg_energy_to_battery_day = ""
        self._etg_energy_to_battery_week = ""
        self._etg_input_frequency = ""
        self._etg_input_voltage = ""
        self._etg_input_current = ""
        self._etg_input_active_power = ""
        self._etg_output_frequency = ""
        self._etg_output_voltage = ""
        self._etg_output_current = ""
        self._etg_output_active_power = ""

    def getTestDescription(self):
        return "New event"

    def getTestCount(self):
        with self._lock:
            return self._test_count

    def setTestCount(self, value):
        with self._lock:
            self._test_count = value
    
    def getEtgBatteryVoltage(self):
        with self._lock:
            return self._etg_battery_voltage

    def setEtgBatteryVoltage(self, value):
        with self._lock:
            self._etg_battery_voltage = value
    
    def getEtgBatteryCurrent(self):
        with self._lock:
            return self._etg_battery_current

    def setEtgBatteryCurrent(self, value):
        with self._lock:
            self._etg_battery_current = value
    
    def getEtgBatteryPower(self):
        with self._lock:
            return self._etg_battery_power

    def setEtgBatteryPower(self, value):
        with self._lock:
            self._etg_battery_power = value
    
    def getEtgBatteryTemperature(self):
        with self._lock:
            return self._etg_battery_temperature

    def setEtgBatteryTemperature(self, value):
        with self._lock:
            self._etg_battery_temperature = value
    
    def getEtgBatteryInvertCurrent(self):
        with self._lock:
            return self._etg_battery_invert_current

    def setEtgBatteryInvertCurrent(self, value):
        with self._lock:
            self._etg_battery_invert_current = value
    
    def getEtgBatteryInvertPower(self):
        with self._lock:
            return self._etg_battery_invert_power

    def setEtgBatteryInvertPower(self, value):
        with self._lock:
            self._etg_battery_invert_power = value
    
    def getEtgBatteryChargeCurrent(self):
        with self._lock:
            return self._etg_battery_charge_current

    def setEtgBatteryChargeCurrent(self, value):
        with self._lock:
            self._etg_battery_charge_current = value
    
    def getEtgBatteryChargePower(self):
        with self._lock:
            return self._etg_battery_charge_power

    def setEtgBatteryChargePower(self, value):
        with self._lock:
            self._etg_battery_charge_power = value
    
    def getEtgChargePowerPercentage(self):
        with self._lock:
            return self._etg_charge_power_percentage

    def setEtgChargePowerPercentage(self, value):
        with self._lock:
            self._etg_charge_power_percentage = value
    
    def getEtgEnergyFromBatteryHour(self):
        with self._lock:
            return self._etg_energy_from_battery_hour

    def setEtgEnergyFromBatteryHour(self, value):
        with self._lock:
            self._etg_energy_from_battery_hour = value
    
    def getEtgEnergyFromBatteryDay(self):
        with self._lock:
            return self._etg_energy_from_battery_day

    def setEtgEnergyFromBatteryDay(self, value):
        with self._lock:
            self._etg_energy_from_battery_day = value
    
    def getEtgEnergyFromBatteryWeek(self):
        with self._lock:
            return self._etg_energy_from_battery_week

    def setEtgEnergyFromBatteryWeek(self, value):
        with self._lock:
            self._etg_energy_from_battery_week = value
    
    def getEtgEnergyToBatteryHour(self):
        with self._lock:
            return self._etg_energy_to_battery_hour

    def setEtgEnergyToBatteryHour(self, value):
        with self._lock:
            self._etg_energy_to_battery_hour = value
    
    def getEtgEnergyToBatteryDay(self):
        with self._lock:
            return self._etg_energy_to_battery_day

    def setEtgEnergyToBatteryDay(self, value):
        with self._lock:
            self._etg_energy_to_battery_day = value
    
    def getEtgEnergyToBatteryWeek(self):
        with self._lock:
            return self._etg_energy_to_battery_week

    def setEtgEnergyToBatteryWeek(self, value):
        with self._lock:
            self._etg_energy_to_battery_week = value
    
    def getEtgInputFrequency(self):
        with self._lock:
            return self._etg_input_frequency

    def setEtgInputFrequency(self, value):
        with self._lock:
            self._etg_input_frequency = value
    
    def getEtgInputVoltage(self):
        with self._lock:
            return self._etg_input_voltage

    def setEtgInputVoltage(self, value):
        with self._lock:
            self._etg_input_voltage = value
    
    def getEtgInputCurrent(self):
        with self._lock:
            return self._etg_input_current

    def setEtgInputCurrent(self, value):
        with self._lock:
            self._etg_input_current = value
    
    def getEtgInputActivePower(self):
        with self._lock:
            return self._etg_input_active_power

    def setEtgInputActivePower(self, value):
        with self._lock:
            self._etg_input_active_power = value
    
    def getEtgOutputFrequency(self):
        with self._lock:
            return self._etg_output_frequency

    def setEtgOutputFrequency(self, value):
        with self._lock:
            self._etg_output_frequency = value
    
    def getEtgOutputVoltage(self):
        with self._lock:
            return self._etg_output_voltage

    def setEtgOutputVoltage(self, value):
        with self._lock:
            self._etg_output_voltage = value
    
    def getEtgOutputCurrent(self):
        with self._lock:
            return self._etg_output_current

    def setEtgOutputCurrent(self, value):
        with self._lock:
            self._etg_output_current = value
    
    def getEtgOutputActivePower(self):
        with self._lock:
            return self._etg_output_active_power

    def setEtgOutputActivePower(self, value):
        with self._lock:
            self._etg_output_active_power = value
    



def createVariable(SuperClass, getValue, *args):
    """This is going to create a instance variable that we can export. 
    getValue is a function to call to retreive the value of the scalar
    """
    class Var(SuperClass):
        def readGet(self, name, *args):
            return name, self.syntax.clone(getValue())
    return Var(*args)


class SNMPAgent(object):
    """Implements an Agent that serves the custom MIB and
    can send a trap.
    """

    def __init__(self, mibObjects):
        """
        mibObjects - a list of MibObject tuples that this agent
        will serve
        """

        #each SNMP-based application has an engine
        self._snmpEngine = engine.SnmpEngine()

        #open a UDP socket to listen for snmp requests
        config.addSocketTransport(self._snmpEngine, udp.domainName,
                                  udp.UdpTransport().openServerMode(('172.16.27.54', 161)))

        #add a v2 user with the community string public
        config.addV1System(self._snmpEngine, "agent", "public")
        #let anyone accessing 'public' read anything in the subtree below,
        #which is the enterprises subtree that we defined our MIB to be in
        config.addVacmUser(self._snmpEngine, 2, "agent", "noAuthNoPriv",
                           readSubTree=(1,3,6,1,4,1))

        #each app has one or more contexts
        self._snmpContext = context.SnmpContext(self._snmpEngine)

        #the builder is used to load mibs. tell it to look in the
        #current directory for our new MIB. We'll also use it to
        #export our symbols later
        mibBuilder = self._snmpContext.getMibInstrum().getMibBuilder()
        mibSources = mibBuilder.getMibSources() + (builder.DirMibSource('.'),)
        mibBuilder.setMibSources(*mibSources)

        #our variables will subclass this since we only have scalar types
        #can't load this type directly, need to import it
        MibScalarInstance, = mibBuilder.importSymbols('SNMPv2-SMI',
                                                      'MibScalarInstance')
        #export our custom mib
        for mibObject in mibObjects:
            nextVar, = mibBuilder.importSymbols(mibObject.mibName,
                                                mibObject.objectType)
            instance = createVariable(MibScalarInstance,
                                      mibObject.valueFunc,
                                      nextVar.name, (0,),
                                      nextVar.syntax)
            #need to export as <var name>Instance
            instanceDict = {str(nextVar.name)+"Instance":instance}
            mibBuilder.exportSymbols(mibObject.mibName,
                                     **instanceDict)

        # tell pysnmp to respotd to get, getnext, and getbulk
        cmdrsp.GetCommandResponder(self._snmpEngine, self._snmpContext)
        cmdrsp.NextCommandResponder(self._snmpEngine, self._snmpContext)
        cmdrsp.BulkCommandResponder(self._snmpEngine, self._snmpContext)


    def setTrapReceiver(self, host, community):
        """Send traps to the host using community string community
        """
        config.addV1System(self._snmpEngine, 'nms-area', community)
        config.addVacmUser(self._snmpEngine, 2, 'nms-area', 'noAuthNoPriv',
                           notifySubTree=(1,3,6,1,4,1))
        config.addTargetParams(self._snmpEngine,
                               'nms-creds', 'nms-area', 'noAuthNoPriv', 1)
        config.addTargetAddr(self._snmpEngine, 'my-nms', udp.domainName,
                             (host, 162), 'nms-creds',
                             tagList='all-my-managers')
        #set last parameter to 'notification' to have it send
        #informs rather than unacknowledged traps
        config.addNotificationTarget(
            self._snmpEngine, 'test-notification', 'my-filter',
            'all-my-managers', 'trap')


    def sendTrap(self, testCount, testDescription, etgBatteryVoltage, etgBatteryCurrent, etgBatteryPower, etgBatteryTemp, etgBatteryInvertCurrent, 
    etgBatteryInvertPower, etgBatteryChargeCurrent, etgBatteryChargePower, etgChargePowerPercentage, etgEnergyFromBatteryHour, etgEnergyFromBatteryDay, etgEnergyFromBatteryWeek,
    etgEnergyToBatteryHour, etgEnergyToBatteryDay, etgEnergyToBatteryWeek, etgInputFrequency, etgInputVoltage, etgInputCurrent, etgInputActivePower, etgOutputFrequency, 
    etgOutputVoltage, etgOutputCurrent, etgOutputActivePower):
        if (etgBatteryVoltage != None and etgBatteryCurrent != None and etgBatteryPower != None and etgBatteryTemp != None and etgBatteryInvertCurrent != None and etgBatteryInvertPower != None 
        and etgBatteryChargeCurrent != None and etgBatteryChargePower != None and etgChargePowerPercentage != None and etgEnergyFromBatteryHour != None and etgEnergyFromBatteryDay != None
        and etgEnergyFromBatteryWeek != None and etgEnergyToBatteryHour != None and etgEnergyToBatteryDay != None and etgEnergyToBatteryWeek != None and etgInputFrequency != None
        and etgInputVoltage != None and etgInputCurrent != None and etgInputActivePower != None and etgOutputFrequency != None and etgOutputVoltage != None and etgOutputCurrent != None
        and etgOutputActivePower != None):
            print ("Sending trap")
            ntfOrg = ntforg.NotificationOriginator(self._snmpContext)
            errorIndication = ntfOrg.sendNotification(
                self._snmpEngine,
                'test-notification',
                ('ETRACK-MIB', 'testTrap'),
                [(rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.2'), rfc1902.OctetString(testDescription)), 
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.1'), rfc1902.Integer(testCount)),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.4'), rfc1902.OctetString(etgBatteryVoltage+' V')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.5'), rfc1902.OctetString(etgBatteryCurrent+' A')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.27'), rfc1902.OctetString(etgBatteryPower+' W')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.7'), rfc1902.OctetString(etgBatteryTemp+' deg.C')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.8'), rfc1902.OctetString(etgBatteryInvertCurrent+' A')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.9'), rfc1902.OctetString(etgBatteryInvertPower+' W')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.10'), rfc1902.OctetString(etgBatteryChargeCurrent+' A')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.11'), rfc1902.OctetString(etgBatteryChargePower+' W')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.12'), rfc1902.OctetString(etgChargePowerPercentage+' %')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.13'), rfc1902.OctetString(etgEnergyFromBatteryHour+' kWh')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.14'), rfc1902.OctetString(etgEnergyFromBatteryDay+' kWh')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.15'), rfc1902.OctetString(etgEnergyFromBatteryWeek+' kWh')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.16'), rfc1902.OctetString(etgEnergyToBatteryHour+' kWh')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.17'), rfc1902.OctetString(etgEnergyToBatteryHour+' kWh')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.18'), rfc1902.OctetString(etgEnergyToBatteryHour+' kWh')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.19'), rfc1902.OctetString(etgInputFrequency+' Hz')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.20'), rfc1902.OctetString(etgInputVoltage+' V')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.21'), rfc1902.OctetString(etgInputCurrent+' A')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.22'), rfc1902.OctetString(etgInputActivePower+' W')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.23'), rfc1902.OctetString(etgOutputFrequency+' Hz')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.24'), rfc1902.OctetString(etgOutputVoltage+' V')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.25'), rfc1902.OctetString(etgOutputCurrent+' A')),
                (rfc1902.ObjectName('1.3.6.1.4.1.76.118.378.26'), rfc1902.OctetString(etgOutputActivePower+' W'))])
        else:
            print ("Cannot send trap because could not get data from remote device")

    def serve_forever(self):
        print ("Starting agent")
        self._snmpEngine.transportDispatcher.jobStarted(1)
        try:
           self._snmpEngine.transportDispatcher.runDispatcher()
        except:
            self._snmpEngine.transportDispatcher.closeDispatcher()
            raise

class Worker(threading.Thread):
    """Just to demonstrate updating the MIB
    and sending traps
    """

    def __init__(self, agent, mib):
        threading.Thread.__init__(self)
        self._agent = agent
        self._mib = mib
        self.setDaemon(True)

    def run(self):
        while True:
            time.sleep(60)
            c = ConextXWSNMPDataCreator(batt = True, pv = True, grid = True, gen = True, load = True, addr = 10)
            etgBatteryVoltage = c.getBatteryVoltage()
            etgBatteryCurrent = c.getBatteryCurrent()
            etgBatteryPower = c.getBatteryPower()
            etgBatteryTemp = c.getBatteryTemperature()
            etgBatteryInvertCurrent = c.getInvertDCCurrent()
            etgBatteryInvertPower = c.getInvertDCPower()
            etgBatteryChargeCurrent = c.getChargeDCCurrent()
            etgBatteryChargePower = c.getChargeDCPower()
            etgChargePowerPercentage = c.getChargeDCPowerPercentage()
            etgEnergyFromBatteryHour = c.getEnergyFromBatteryHour()
            etgEnergyFromBatteryDay = c.getEnergyFromBatteryToday()
            etgEnergyFromBatteryWeek = c.getEnergyFromBatteryWeek()
            etgEnergyToBatteryHour = c.getEnergyToBatteryHour()
            etgEnergyToBatteryDay = c.getEnergyToBatteryToday()
            etgEnergyToBatteryWeek = c.getEnergyToBatteryWeek()
            etgInputFrequency = c.getGridACFrequency()
            etgInputVoltage = c.getGridACVoltage()
            etgInputCurrent = c.getGridACCurrent()
            etgInputActivePower = c.getGridACInputPower()
            etgOutputFrequency = c.getGridOutputFrequency()
            etgOutputVoltage = c.getGridOutputVoltage()
            etgOutputCurrent = c.getGridOutputCurrent()
            etgOutputActivePower = c.getGridOutputPower()
            self._mib.setTestCount(mib.getTestCount()+1)
            self._mib.setEtgBatteryVoltage(etgBatteryVoltage)
            self._mib.setEtgBatteryCurrent(etgBatteryCurrent)
            self._mib.setEtgBatteryPower(etgBatteryPower)
            self._mib.setEtgBatteryTemperature(etgBatteryTemp)
            self._mib.setEtgBatteryInvertCurrent(etgBatteryInvertCurrent)
            self._mib.setEtgBatteryInvertPower(etgBatteryInvertPower)
            self._mib.setEtgBatteryChargeCurrent(etgBatteryChargeCurrent)
            self._mib.setEtgBatteryChargePower(etgBatteryChargePower)
            self._mib.setEtgChargePowerPercentage(etgChargePowerPercentage)
            self._mib.setEtgEnergyFromBatteryHour(etgEnergyFromBatteryHour)
            self._mib.setEtgEnergyFromBatteryDay(etgEnergyFromBatteryDay)
            self._mib.setEtgEnergyFromBatteryWeek(etgEnergyFromBatteryWeek)
            self._mib.setEtgEnergyToBatteryHour(etgEnergyToBatteryHour)
            self._mib.setEtgEnergyToBatteryDay(etgEnergyToBatteryDay)
            self._mib.setEtgEnergyToBatteryWeek(etgEnergyToBatteryWeek)
            self._mib.setEtgInputFrequency(etgInputFrequency)
            self._mib.setEtgInputVoltage(etgInputVoltage)
            self._mib.setEtgInputCurrent(etgInputCurrent)
            self._mib.setEtgInputActivePower(etgInputActivePower)
            self._mib.setEtgOutputFrequency(etgOutputFrequency)
            self._mib.setEtgOutputVoltage(etgOutputVoltage)
            self._mib.setEtgOutputCurrent(etgOutputCurrent)
            self._mib.setEtgOutputActivePower(etgOutputActivePower)
            self._agent.sendTrap(mib.getTestCount()+1, "New event", etgBatteryVoltage, etgBatteryCurrent, etgBatteryPower, etgBatteryTemp, etgBatteryInvertCurrent, 
            etgBatteryInvertPower, etgBatteryChargeCurrent, etgBatteryChargePower, etgChargePowerPercentage, etgEnergyFromBatteryHour, etgEnergyFromBatteryDay,
            etgEnergyFromBatteryWeek, etgEnergyToBatteryHour, etgEnergyToBatteryDay, etgEnergyToBatteryWeek, etgInputFrequency, etgInputVoltage, etgInputCurrent, 
            etgInputActivePower, etgOutputFrequency, etgOutputVoltage, etgOutputCurrent, etgOutputActivePower)

if __name__ == '__main__':
    mib = Mib()

    objects = [
        MibObject('ETRACK-MIB', 'testDescription', mib.getTestDescription()), 
    MibObject('ETRACK-MIB', 'testCount', mib.getTestCount()),
    MibObject('ETRACK-MIB', 'etgBatteryVoltage', mib.getEtgBatteryVoltage()),
    MibObject('ETRACK-MIB', 'etgBatteryCurrent', mib.getEtgBatteryCurrent()),
    MibObject('ETRACK-MIB', 'etgBatteryPower', mib.getEtgBatteryPower()),
    MibObject('ETRACK-MIB', 'etgBatteryTemperature', mib.getEtgBatteryTemperature()),
    MibObject('ETRACK-MIB', 'etgBatteryInvertCurrent', mib.getEtgBatteryInvertCurrent()),
    MibObject('ETRACK-MIB', 'etgBatteryInvertPower', mib.getEtgBatteryInvertPower()),
    MibObject('ETRACK-MIB', 'etgBatteryChargeCurrent', mib.getEtgBatteryChargeCurrent()),
    MibObject('ETRACK-MIB', 'etgBatteryChargePower', mib.getEtgBatteryChargePower()),
    MibObject('ETRACK-MIB', 'etgChargePowerPercentage', mib.getEtgChargePowerPercentage()),
    MibObject('ETRACK-MIB', 'etgEnergyFromBatteryHour', mib.getEtgEnergyFromBatteryHour()),
    MibObject('ETRACK-MIB', 'etgEnergyFromBatteryDay', mib.getEtgEnergyFromBatteryDay()),
    MibObject('ETRACK-MIB', 'etgEnergyFromBatteryWeek', mib.getEtgEnergyFromBatteryWeek()),
    MibObject('ETRACK-MIB', 'etgEnergyToBatteryHour', mib.getEtgEnergyToBatteryHour()),
    MibObject('ETRACK-MIB', 'etgEnergyToBatteryDay', mib.getEtgEnergyToBatteryDay()),
    MibObject('ETRACK-MIB', 'etgEnergyToBatteryWeek', mib.getEtgEnergyToBatteryWeek()),
    MibObject('ETRACK-MIB', 'etgInputFrequency', mib.getEtgInputFrequency()),
    MibObject('ETRACK-MIB', 'etgInputVoltage', mib.getEtgInputVoltage()),
    MibObject('ETRACK-MIB', 'etgInputCurrent', mib.getEtgInputCurrent()),
    MibObject('ETRACK-MIB', 'etgInputActivePower', mib.getEtgInputActivePower()),
    MibObject('ETRACK-MIB', 'etgOutputFrequency', mib.getEtgOutputFrequency()),
    MibObject('ETRACK-MIB', 'etgOutputVoltage', mib.getEtgOutputVoltage()),
    MibObject('ETRACK-MIB', 'etgOutputCurrent', mib.getEtgOutputCurrent()),
    MibObject('ETRACK-MIB', 'etgOutputActivePower', mib.getEtgOutputActivePower())]
    agent = SNMPAgent(objects)
    agent.setTrapReceiver('172.16.26.217', 'traps')
    Worker(agent, mib).start()
    try:
        agent.serve_forever()
    except KeyboardInterrupt:
        print ("Shutting down")
