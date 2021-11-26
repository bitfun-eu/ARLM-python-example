from pip import main

def install(cmd):
    main(['install'] + cmd.split())

install('pyserial')
