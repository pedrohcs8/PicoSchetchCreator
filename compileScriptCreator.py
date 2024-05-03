createScript = [
  'rm -rf build/*\n',
  'cd build\n',
  'cmake ..\n',
  'bear -- make\n',
  '$shell\n'
]

def createCompileScript(projectDir):
  compileScript = open(projectDir + '/compile.sh', 'x')

  compileScript.writelines(createScript)
  compileScript.close()
