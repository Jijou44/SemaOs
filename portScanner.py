import nmap

def scanHost():
    host = input("Enter the host to scan: ")
    port = input("Enter the port range to scan: | Ex: 22-443 | ")

    nm = nmap.PortScanner()
    nm.scan(host, port)
    nm.scaninfo()


    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            print(nm[host][proto])
            lport = nm[host][proto].keys()
            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

