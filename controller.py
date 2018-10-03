import model
import renderer
import connector


class SocialMedia:

    def __init__(self):
        self.renderer = renderer.StubMessageRenderer()
        self.facebook_connector = connector.FacebookConnector()
        self.sms_connector = connector.SMSConnector()

    def alert_authorities(self, incident: model.Incident):
        pass

    def alert_public(self, incident: model.Incident):
        pass

    def post_facebook(self, incident: model.Incident):
        self.facebook_connector.send_message(self.renderer.render_message(incident))
