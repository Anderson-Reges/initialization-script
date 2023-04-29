import subprocess


output = subprocess.check_output(['ls', '-a'])

# Imprima a saída
print(output.decode('utf-8'))
