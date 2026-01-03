import socket

def scan_ports(target, ports):
    results = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"

                results.append({
                    "port": port,
                    "service": service.upper()
                })

            sock.close()
        except Exception:
            pass

    return results

