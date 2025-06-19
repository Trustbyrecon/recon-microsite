class GhostLog:
    def __init__(self):
        self.entries = []

    def record(self, data):
        self.entries.append(data)
