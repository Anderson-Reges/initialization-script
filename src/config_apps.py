import pickle


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.apps = []

    def add_app(self, app):
        self.apps.append(app)
        self._save()

    def remove_app(self, app):
        self.apps.remove(app)
        self._save()

    def get_apps(self):
        return self.apps

    def _save(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.apps, f)

    def load(self):
        try:
            with open(self.filename, 'rb') as f:
                self.apps = pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo não encontrado")
