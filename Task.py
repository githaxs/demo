class Task():
    def __init__(self, token: str):
        self.token = token
        print("I have initialized")

        return True

    def handle(self, request):
        return request
