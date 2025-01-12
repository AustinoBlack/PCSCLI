def show_general_help():
    """
    Displays a general help message for the CLI.
    """
    print("""
Cluster CLI - General Help
========================================================
This command-line interface allows you to manage your Proxmox cluster via serial commands.

Basic Commands:
    help        Display this general help message.
    clear       Clears the screen.
    exit        Exits the Cluster CLI.

Using the -help Flag:
    Add the -help flag to any valid command to see detailed usage instructions.

Advanced Commands:
    pcscli      Manage power, reset, and basic node operations.
    sh          Retrieve system information for nodes.
    set         Configure system settings, including boot options, LEDs, and FRU.

Version Information:
    PCSCLI Version: 0.1.0
    Author: Austin Black
    License: MIT
    """)


def show_help(prefix, command):
    """
    Displays the help message for a given prefix and command.

    Args:
        prefix (str): The command prefix (e.g., pcscli, sh, set).
        command (str): The specific command to show help for.
    """
    print(str(prefix) + " " + str( command ) )
    if prefix == "pcscli":
        if command == "-help":
            pcscli_general_help()
        elif command == "setpoweron":
            setpoweron_help()

    elif prefix == "sh":
        if command == "-help":
            sh_general_help()

    elif prefix == "set":
        if command == "-help":
            set_general_help()


def pcscli_general_help():
    print("pcscli general help")

def setpoweron_help():
    print("set power on help")

def sh_general_help():
    print("sh general help")

def set_general_help():
    print("set general help")
