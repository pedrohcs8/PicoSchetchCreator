import numpy

cmakeFileScript = [
  '# Set Minimum Cmake Version\n',
  'cmake_minimum_required(VERSION 3.12)\n',
  '\n',
  '# Include Build Functions\n',
  'include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)\n',
  '\n',
  'DYNAMICALLY REPLACED PROJECT',
  'set(CMAKE_C_STANDARD 11)\n',
  'set(CMAKE_CXX_STANDARD 17)\n',
  '\n',
  'pico_sdk_init()\n',
  '\n',
  'add_executable(${PROJECT_NAME}\n',
  '    main.c\n',
  ')\n',
  '\n',
  'pico_enable_stdio_usb(${PROJECT_NAME} 1)\n',
  'pico_enable_stdio_uart(${PROJECT_NAME} 0)\n',
  '\n',
  '# Make UF2\n',
  'pico_add_extra_outputs(${PROJECT_NAME})\n',
  '\n',
  '# Link to STDLIB\n',
  'target_link_libraries(${PROJECT_NAME}\n',
  '    pico_stdlib\n',
  ')\n',
  '\n',
  'add_compile_definitions(PICO_STDIO_USB_CONNECT_WAIT_TIMEOUT_MS=5000)',
]

def createCMakeFile(projectDir, isI2C):
  cmakeFile = open(projectDir + '/CMakeLists.txt', 'x')

  convArray = numpy.array(cmakeFileScript)
  convArray[6] = 'project(' + projectDir + ' C CXX ASM)\n'

  if (isI2C):
    convArray = numpy.insert(convArray, 25, '    hardware_i2c\n')

  cmakeFile.writelines(convArray)

  cmakeFile.close()

