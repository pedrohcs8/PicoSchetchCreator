createScript = [
  'rm -rf build/*\n',
  'cd build\n',
  'cmake ..\n',
  'bear -- make\n',
  'rm -rf ../compile_commands.json\n'
  'cp compile_commands.json ..\n'
  '$shell\n'
]

def createCompileScript(projectDir):
  compileScript = open(projectDir + '/compile.sh', 'x')

  compileScript.writelines(createScript)
  compileScript.close()
