def ip_address(address):
    new_address = ""
    split_address = address.split(".") #splits the ip address and makes values as elements of list
    separator = "[.]"
    new_address = separator.join(split_address) #again join elements of the address to make string again
    return new_address
    
ipaddress = ip_address("1.1.2.3")
print(ipaddress)