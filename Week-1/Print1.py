hostname = "R1"
interface = "GigabitEthernet0/0"
ip_address = "192.168.1.1"
subnet_mask = "255.255.255.0"

# f-strings: the most important string tool in network automation
print(f"Interface {interface} on {hostname} has IP {ip_address}/{subnet_mask}")

# String methods you'll use daily
output = "GigabitEthernet0/0 is up, line protocol is up"
print(output.split(","))  # Split on comma
print("up" in output)  # Check if string contains word
print(output.replace("up", "UP"))  # Replace text
