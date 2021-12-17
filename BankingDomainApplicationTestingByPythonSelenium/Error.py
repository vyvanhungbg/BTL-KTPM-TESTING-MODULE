class ValidationError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
    def __str__(self):
        return self.message