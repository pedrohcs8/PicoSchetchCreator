# PicoSchetchCreator

A simple program for creating projects for the Raspberry Pi Pico, focusing on lsp based editors like vim and nvim, with built in creation of compile_commands.json using [rizsotto/Bear](https://github.com/rizsotto/Bear)

**Requirements:**

[bear](https://github.com/rizsotto/Bear)

Python 3.10

minicom (optional)

**Install**

Simply clone the repo or download standalone-creator.py

<code>git clone https://github.com/pedrohcs8/PicoSchetchCreator</code>

**Usage:**

Simply run the standalone-creator.py file, optionally go to src and run main.py

<code>python3 standalone-creator.py</code>
OR
<code>python3 src/main.py</code>

This will automatically create the project in the same foder it was runned, creating a main script, a compile script and a script for serial monitoring with minicom on /dev/ttyACM0, all being sh, additionaly it will do the first compiling, giving you the compile_commands.json file, important for autocompletion with lsp's
