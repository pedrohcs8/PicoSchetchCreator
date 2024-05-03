# TODO: Make i2c schetch generation

import os
import shutil

from compileScriptCreator import *
from serialMonitorScriptCreator import *
from CMakeCreator import *
from mainFileCreator import *

projectDir = input('Project Name: ')
useI2C = input('Use I2C Library? (y/n): ').lower().strip() == 'y'

os.mkdir(projectDir)

createCompileScript(projectDir)
createSerialMonitorScript(projectDir)
createCMakeFile(projectDir, useI2C)
createMainFile(projectDir, useI2C)

os.mkdir(projectDir + '/build')

os.chdir(projectDir)
os.system('sh ' + 'compile.sh')

shutil.copy2('build/compile_commands.json', '.')
