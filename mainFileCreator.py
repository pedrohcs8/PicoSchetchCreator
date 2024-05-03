import numpy

mainFileScript = [
  '#include <stdio.h>\n',
  '#include "pico/stdlib.h"\n',
  '\n',
  'int main() {\n',
  '  return 0;\n',
  '}\n',
]

def createMainFile(projectDir, isI2C):
  mainFile = open(projectDir + '/main.c', 'x')

  writeArray = numpy.array(mainFileScript)

  if (isI2C):
    writeArray = numpy.insert(writeArray, 2, ['#include "hardware/i2c.h"', '\n'])

  mainFile.writelines(writeArray)

  mainFile.close()
