class Incident:

    def __init__(self, identifier, name):
        self.id = identifier
        self.name = name
        self.category = None
        self.latitude = None
        self.longitude = None
        self.description = None
        self.date = None
        self.time = None
        self.advisory = None
