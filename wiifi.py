import scapy.all as scapy
import optparse as op

def user_parametres():
    options = op.OptionParser()
    options.add_option("-r", "--range", dest="range", help="Type ip range e.g. 192.168.1.1/24, 10.0.1.1/24")
    (user_input, arguments) = options.parse_args()
    if not user_input.range:
        print("You must enter ip range")
        exit()
    return user_input
def scanning(range):
    request = scapy.ARP(pdst=range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    rb = broadcast/request
    (answered_list, unanswered_list) = scapy.srp(rb, timeout=1)
    answered_list.summary()

ip_range = user_parametres()
scanning(ip_range.range)