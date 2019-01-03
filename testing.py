from Firewall import Firewall
import unittest


firewall = Firewall("table.csv")
#given tests
print(firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(firewall.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(firewall.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(firewall.accept_packet("inbound", "udp", 24, "52.12.48.92"))

#test for low port num
print(firewall.accept_packet("outbound", "tcp", 999, "192.168.10.11"))
#test for high port num
print(firewall.accept_packet("outbound", "tcp", 200001, "192.168.10.11"))
#test for high ip
print(firewall.accept_packet("inbound", "udp", 53, "192.168.2.6"))
#test for low ip
print(firewall.accept_packet("inbound", "udp", 53, "192.168.1.0"))
