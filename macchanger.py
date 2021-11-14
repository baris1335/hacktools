import subprocess
import optparse as op
import re as regex

def user_parametres():
    options = op.OptionParser()
    options.add_option("-i", "--interface", dest="interface", help="Select interface")
    options.add_option("-m", "--macaddr", dest="mac", help="Type mac address")

    return options.parse_args()

def old_mac(interface, mac):
    mac_control = subprocess.check_output(["ifconfig", interface])
    old_macaddr = regex.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(mac_control))
    if old_macaddr.group(0) == mac:
        print("Your mac is already " + old_macaddr.group(0))
        exit()
    else:
       return None

def macaddr_change(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def check(interface, mac):
    mac_control = subprocess.check_output(["ifconfig", interface])
    new_mac = regex.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(mac_control))
    if new_mac.group(0) == mac:
        print("Your new mac address is " + new_mac.group(0))
    else:
       print("Error while changing mac addres.")

print("MacChanger is started.")
(user_input, arguments) = user_parametres()
old_mac(user_input.interface, user_input.mac)
macaddr_change(user_input.interface, user_input.mac)
check(user_input.interface, user_input.mac)

print("MacChanger is finished")
