class Customer:
    def __init__(self, details):
        self.details = details

    def to_dict(self):
        return self.details
