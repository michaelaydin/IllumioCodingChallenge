import csv

class Firewall(object):

    rules = {}
    #store rules in a dictionary of dictionaries
    def __init__(self, path):
        self.rules["inbound"] = {}
        self.rules["outbound"] = {}
        self.rules["inbound"]["tcp"] = {}
        self.rules["outbound"]["tcp"] = {}
        self.rules["inbound"]["udp"] = {}
        self.rules["outbound"]["udp"] = {}

        #https://realpython.com/python-csv/ on reminder how to go through csvs
        csv_file = open(path, mode = 'r', encoding='utf-8-sig')
        #encoding was a weird bug fixed using stackoverflow
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            direction = row[0]
            protocol = row[1]
            port = row[2]
            ip_address = row[3]

            port_dictionary = self.rules[direction][protocol]
            if port in port_dictionary:
                self.rules[direction][protocol][port] += ip_address
            else:
                self.rules[direction][protocol][port] = ip_address

    def accept_packet(self, direction, protocol, port, ip_address):
        if not self.rules[direction][protocol]:
            return False
        port_dictionary = self.rules[direction][protocol]
        #print(port_dictionary)
        for port_rule, ip_rules in port_dictionary.items():
            if self.valid_port(port_rule, port):
                if self.valid_ip(ip_rules, ip_address):
                    return True
                else:
                    return False
            else:
                return False

    def valid_port(self, port_rule, check_port):
        #which format
        dash = port_rule.find("-")
        if dash == -1:
            if int(port_rule) == int(check_port):
                return True
            else:
                return False
        else:
            predash = int(port_rule[:dash])
            postdash = int(port_rule[dash+1:])
            #caught bug first in valid_ip, again weird thing,
            #can't must use nested if statement
            if int(check_port) <= postdash:
                if int(check_port) >= predash:
                    return True
            else:
                return False

    def valid_ip(self, ip_rule, check_ip):
        dash = ip_rule.find("-")
        if dash == -1:
            #print(ip_rule)
            #print(check_ip)
            if ip_rule == check_ip:
                return True
            else:
                return False
        else:
            predash = int(ip_rule[:dash].replace(".", ""))
            postdash = int(ip_rule[dash+1:].replace(".", ""))
            check_ip = int(check_ip.replace(".",""))
            #print(predash)
            #print(postdash)
            #print(check_ip <= postdash & check_ip >= predash)
            #no idea why this bug is happening, caught using above print statement
            #for some reason have to do nested if statement instead of one with an &
            if check_ip <= postdash:
                if check_ip >= predash:
                    return True
            else:
                return False
