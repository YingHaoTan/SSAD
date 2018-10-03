class APIConnector:

    def send_message(self, message: str):
        raise NotImplementedError("send_message method is not implemented")


class SMSConnector(APIConnector):

    def send_message(self, message: str):
        pass


class FacebookConnector(APIConnector):

    def send_message(self, message: str):
        pass
