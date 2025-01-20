import numpy

mainFileScript = [ 
  '\n',
  'int main() {\n',
  '  return 0;\n',
  '}\n',
]

def createMainFile(projectDir, isI2C, isPWM, isADC, isGPIO):
  mainFile = open(projectDir + '/main.c', 'x')

  topLines = 1

  mainFile.write('#include <stdio.h>\n')
  mainFile.write('#include "pico/stdlib.h"\n')

  if (isI2C):
    mainFile.write('#include "hardware/i2c.h"\n');

  if (isPWM):
    mainFile.write('#include "hardware/pwm.h"\n')

  if (isADC):
    mainFile.write('#include "hardware/adc.h"\n')

  if (isGPIO):
    mainFile.write('#include "hardware/gpio.h"\n')

  writeArray = numpy.array(mainFileScript)
  mainFile.writelines(writeArray)

  mainFile.close()
