# TODO: Make i2c schetch generation

import os
import shutil

from fileScripts.compileScriptCreator import *
from fileScripts.serialMonitorScriptCreator import *
from fileScripts.CMakeCreator import *
from fileScripts.mainFileCreator import *

projectDir = input('Project Name: ')
useI2C = input('Use I2C Library? (y/n): ').lower().strip() == 'y'
usePWM = input('Use PWM Library? (y/n): ').lower().strip() == 'y'
useGPIO = input('Use GPIO Library? (y/n): ').lower().strip() == 'y'
useADC = input('Use ADC Library? (y/n): ').lower().strip() == 'y'

os.mkdir(projectDir)

createCompileScript(projectDir)
createSerialMonitorScript(projectDir)

createCMakeFile(projectDir, useI2C, usePWM, useADC, useGPIO)
createMainFile(projectDir, useI2C, usePWM, useADC, useGPIO)

os.mkdir(projectDir + '/build')

os.chdir(projectDir)
os.system('sh ' + 'compile.sh')

shutil.copy2('build/compile_commands.json', '.')
