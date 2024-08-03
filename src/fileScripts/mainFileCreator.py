import numpy

mainFileScript = [
  '#include <stdio.h>\n',
  '#include "pico/stdlib.h"\n',
  '\n',
  'int main() {\n',
  '  return 0;\n',
  '}\n',
]

def createMainFile(projectDir, isI2C, isPWM, isADC, isGPIO):
  mainFile = open(projectDir + '/main.c', 'x')

  writeArray = numpy.array(mainFileScript)

  topLines = 1

  if (isI2C):
    topLines = topLines + 1
    writeArray = numpy.insert(writeArray, topLines, ['#include "hardware/i2c.h"', '\n'])

  if (isPWM):
    topLines = topLines + 1
    writeArray = numpy.insert(writeArray, topLines, ['#include "hardware/pwm.h"', '\n'])

  if (isADC):
    topLines = topLines + 1
    writeArray = numpy.insert(writeArray, topLines, ['#include "hardware/adc.h"', '\n'])

  if (isGPIO):
    topLines = topLines + 1
    writeArray = numpy.insert(writeArray, topLines, ['#include "hardware/gpio.h"', '\n'])

  mainFile.writelines(writeArray)

  mainFile.close()
