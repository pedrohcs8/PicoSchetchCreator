# PicoSchetchCreator

This is a simple script aimed for making your life easier when creating new projects involving the Raspberry Pi Pico and its C SDK, by providing a simple barebones template creator

# Requirements

[Build EAR](https://github.com/rizsotto/Bear) - Used to create compile_commands.json for clangd completion

Pico C SDK Installer (Debian Only for other distros install manually)

Install Requirements:  

    sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y

Use the installer:

    wget https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh

# Instalation:

    pip install -r requirements.txt

Then you can use either the standalone or the unpacked version of the program

# Use

    python3 main.py

    OR

    python3 standalone-creator.py
