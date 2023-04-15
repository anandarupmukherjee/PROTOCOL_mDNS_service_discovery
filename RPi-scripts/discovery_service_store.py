import time
import sqlite3
import socket
from zeroconf import ServiceBrowser, Zeroconf

# Define a function to handle service events
def on_service_state_change(zeroconf, service_type, name, state_change):
    # Get the current timestamp
    timestamp = int(time.time())

    # Get the service information
    info = zeroconf.get_service_info(service_type, name)
    print(info)

    if info != None:

        # Extract the properties from the service information
        owner = info.properties.get(b'owner', b'').decode('utf-8')
        mac_address = info.properties.get(b'mac_address', b'').decode('utf-8')
        device_type = info.properties.get(b'device_type', b'').decode('utf-8')
        
        address_str = socket.inet_ntoa(info.addresses[0])
        ip_address = address_str
        # print(ip_address)


        # Open a connection to the SQLite database
        conn = sqlite3.connect('mdns_services.db')
        cursor = conn.cursor()

        # Insert the service information and properties into the database
        cursor.execute("INSERT INTO services (name, type, domain, address, port, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                    (mac_address, info.server, owner, ip_address, info.port, timestamp))
        conn.commit()






        # Close the database connection
        conn.close()

# Set up the Zeroconf service browser
zeroconf = Zeroconf()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", handlers=[on_service_state_change])

# Keep running until the user interrupts the program
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Clean up and exit
zeroconf.close()
