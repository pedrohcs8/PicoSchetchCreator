#!/usr/bin/env python
import contextlib as __stickytape_contextlib

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path

        def make_package(path):
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    with open(os.path.join(partial_path, "__init__.py"), "wb") as f:
                        f.write(b"\n")

        make_package(os.path.dirname(path))

        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "wb") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

    __stickytape_write_module('fileScripts/compileScriptCreator.py', b"createScript = [\n  'rm -rf build/*\\n',\n  'cd build\\n',\n  'cmake ..\\n',\n  'bear -- make\\n',\n  '$shell\\n'\n]\n\ndef createCompileScript(projectDir):\n  compileScript = open(projectDir + '/compile.sh', 'x')\n\n  compileScript.writelines(createScript)\n  compileScript.close()\n")
    __stickytape_write_module('fileScripts/serialMonitorScriptCreator.py', b"serialMonitorScript = [\n  'sudo minicom -b 115200 -o -D /dev/ttyACM0'\n]\n\ndef createSerialMonitorScript(projectDir):\n  serialMonitorScriptFile = open(projectDir + '/serialmonitor.sh', 'x')\n\n  serialMonitorScriptFile.writelines(serialMonitorScript)\n  serialMonitorScriptFile.close()\n\n")
    __stickytape_write_module('fileScripts/CMakeCreator.py', b"import numpy\n\ncmakeFileScript = [\n  '# Set Minimum Cmake Version\\n',\n  'cmake_minimum_required(VERSION 3.12)\\n',\n  '\\n',\n  '# Include Build Functions\\n',\n  'include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)\\n',\n  '\\n',\n  'DYNAMICALLY REPLACED PROJECT',\n  'set(CMAKE_C_STANDARD 11)\\n',\n  'set(CMAKE_CXX_STANDARD 17)\\n',\n  '\\n',\n  'pico_sdk_init()\\n',\n  '\\n',\n  'add_executable(${PROJECT_NAME}\\n',\n  '    main.c\\n',\n  ')\\n',\n  '\\n',\n  'pico_enable_stdio_usb(${PROJECT_NAME} 1)\\n',\n  'pico_enable_stdio_uart(${PROJECT_NAME} 0)\\n',\n  '\\n',\n  '# Make UF2\\n',\n  'pico_add_extra_outputs(${PROJECT_NAME})\\n',\n  '\\n',\n  '# Link to STDLIB\\n',\n  'target_link_libraries(${PROJECT_NAME}\\n',\n  '    pico_stdlib\\n',\n  ')\\n',\n  '\\n',\n  'add_compile_definitions(PICO_STDIO_USB_CONNECT_WAIT_TIMEOUT_MS=5000)',\n]\n\ndef createCMakeFile(projectDir, isI2C, isPWM, isADC, isGPIO):\n  cmakeFile = open(projectDir + '/CMakeLists.txt', 'x')\n\n  convArray = numpy.array(cmakeFileScript)\n  convArray[6] = 'project(' + projectDir + ' C CXX ASM)\\n'\n\n  topLines = 24;\n\n  if (isI2C):\n    topLines = topLines + 1\n    convArray = numpy.insert(convArray, 25, '    hardware_i2c\\n')\n\n  if (isPWM):\n    topLines = topLines + 1\n    convArray = numpy.insert(convArray, 25, '    hardware_pwm\\n')\n\n  if (isADC):\n    topLines = topLines + 1\n    convArray = numpy.insert(convArray, 25, '    hardware_adc\\n')\n\n  if (isGPIO):\n    topLines = topLines + 1\n    convArray = numpy.insert(convArray, 25, '    hardware_gpio\\n')\n\n  cmakeFile.writelines(convArray)\n\n  cmakeFile.close()\n\n")
    __stickytape_write_module('fileScripts/mainFileCreator.py', b'import numpy\n\nmainFileScript = [\n  \'#include <stdio.h>\\n\',\n  \'#include "pico/stdlib.h"\\n\',\n  \'\\n\',\n  \'int main() {\\n\',\n  \'  return 0;\\n\',\n  \'}\\n\',\n]\n\ndef createMainFile(projectDir, isI2C, isPWM, isADC, isGPIO):\n  mainFile = open(projectDir + \'/main.c\', \'x\')\n\n  writeArray = numpy.array(mainFileScript)\n\n  topLines = 1\n\n  if (isI2C):\n    topLines = topLines + 1\n    writeArray = numpy.insert(writeArray, topLines, [\'#include "hardware/i2c.h"\', \'\\n\'])\n\n  if (isPWM):\n    topLines = topLines + 1\n    writeArray = numpy.insert(writeArray, topLines, [\'#include "hardware/pwm.h"\', \'\\n\'])\n\n  if (isADC):\n    topLines = topLines + 1\n    writeArray = numpy.insert(writeArray, topLines, [\'#include "hardware/adc.h"\', \'\\n\'])\n\n  if (isGPIO):\n    topLines = topLines + 1\n    writeArray = numpy.insert(writeArray, topLines, [\'#include "hardware/gpio.h"\', \'\\n\'])\n\n  mainFile.writelines(writeArray)\n\n  mainFile.close()\n')
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
    