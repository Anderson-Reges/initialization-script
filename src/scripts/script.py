import subprocess


# Execute o comando "ls" no shell e capture a saída
output = subprocess.check_output(['ls', '-a'])

# Imprima a saída
print(output.decode('utf-8'))
