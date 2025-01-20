import getpass

createScript = [
  'rm -rf build/*\n',
  'cd build\n',
  'cmake ..\n',
  'bear -- make\n',
  'rm -rf ../compile_commands.json\n'
  'cp compile_commands.json ..\n'
]

def createCompileScript(projectDir):
  compileScript = open(projectDir + '/compile.sh', 'x')

  compileScript.writelines(createScript)

  compileScript.write('cp ' + projectDir + '.uf2 ' + '/media/' + getpass.getuser() + '/RPI-RP2\n')
  compileScript.write('$shell\n')

  compileScript.close()
