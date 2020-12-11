#
# PySNMP MIB module MY-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///root/Etrack_SNMP/MY-MIB
# Produced by pysmi-0.0.6 at Mon Dec  7 17:12:57 2020
# On host HO-CASNMPBUS platform Linux version 3.10.0-1160.2.2.el7.x86_64 by user root
# Using Python version 2.7.5 (default, Aug 13 2020, 02:51:10) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myCompany = MibIdentifier((1, 3, 6, 1, 4, 1, 72))
testCount = MibScalar((1, 3, 6, 1, 4, 1, 72, 1), Integer32()).setMaxAccess("readonly")
testDescription = MibScalar((1, 3, 6, 1, 4, 1, 72, 2), OctetString()).setMaxAccess("readonly")
testTrap = NotificationType((1, 3, 6, 1, 4, 1, 72, 3)).setObjects(*())
mibBuilder.exportSymbols("MY-MIB", testCount=testCount, testDescription=testDescription, myCompany=myCompany, testTrap=testTrap)
