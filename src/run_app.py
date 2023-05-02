import subprocess

# para achar no Flatpak: flatpak list | grep nome-do-app
# Para achar no apt : dpkg -s nome-do-app


def run_app(app_name):
    try:
        apt, flatpak = check_package_app(app_name)
        if apt:
            subprocess.Popen(
                ["nohup", "bash", "-c", f"exec /usr/bin/{app_name}", "&"]
            )
        else:
            command = ["flatpak", "list"]
            grep_command = ["grep", f"{app_name}"]

            output1 = subprocess.check_output(command)
            output2 = subprocess.check_output(grep_command, input=output1)
            app_flatpak_id = output2.decode().split()[1]

            subprocess.Popen(
                ["nohup", "flatpak", "run", app_flatpak_id, ]
            )
    except subprocess.CalledProcessError as e:
        return print(f"Erro ao ativo o aplicativo {app_name}: {e}")


def check_package_app(app_name):
    apt = check_apt(app_name)
    flatpak = check_flatpak(app_name)

    return [apt, flatpak]


def check_apt(app_name):
    try:
        subprocess.check_output(['dpkg', '-s', f'{app_name}'])
        return True
    except subprocess.CalledProcessError:
        return False


def check_flatpak(app_name):
    try:
        command = ["flatpak", "list"]
        grep_command = ["grep", f"{app_name}"]

        output1 = subprocess.check_output(command)
        output2 = subprocess.check_output(grep_command, input=output1)
        if output2:
            output_str = output2.decode("utf-8")
            if output_str:
                return True
        else:
            print(
                f"O aplicativo '{app_name}' não foi encontrado no Flatpak."
            )
    except subprocess.CalledProcessError:
        return False
