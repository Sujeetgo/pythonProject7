#!/user/bin/python3
import nmap
scanner=nmap.PortScanner()

print("Welcome ,this is simple nmap automation tool")
print("<------------------------------------------------>")
ip_addr=input("please enter the IP address you want to scan:")

print("your enter IP address is:",ip_addr)
type(ip_addr)

resp=input("""\nPlease enter the type of scan you want to run
              1)SYK ACK scan
              2)UDP scan
              Comprehensive scan\n""")
print("you have selected option: ",resp)
if resp=='1':
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_addr,'1-0124','-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ",scanner[ip_addr]['tcp'].keys())
elif resp=='2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-0124', '-v -sU')
    print(scanner.scaninfo())
    print("Ip status: ",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ",scanner[ip_addr]['udp'].keys())
elif resp=='3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-0124', '-v -sS -sV -sC -A -o')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

else:
    print("please enter a valid option")







