import subprocess


def run_app(app_name):
    try:
        result = subprocess.run(
            ["xdotool", "search", "--name", app_name],
            stdout=subprocess.PIPE,
            check=True
        )
        app_id = result.stdout.decode().strip()
        subprocess.run(["xdotool", "windowactivate", app_id], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao ativar o aplicativo {app_name}: {e}")
