def server_config_update(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)   

server_config_file = 'server.conf'

key_to_update = 'TIMEOUT'
new_value = '60' 

server_config_update(server_config_file, key_to_update, new_value)                        
