serialMonitorScript = [
  'sudo minicom -b 115200 -o -D /dev/ttyACM0'
]

def createSerialMonitorScript(projectDir):
  serialMonitorScriptFile = open(projectDir + '/serialmonitor.sh', 'x')

  serialMonitorScriptFile.writelines(serialMonitorScript)
  serialMonitorScriptFile.close()

