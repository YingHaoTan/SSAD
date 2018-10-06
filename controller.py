import model
import renderer
import connector

ALERT_AUTHORITY_SPEC = """
Crisis Management System

The following incident was recorded and assistance is required from your department.

Incident Name: 
{0.name}

Incident Category: 
{0.category}

Description:
{0.description}
"""


ALERT_PUBLIC_SPEC = """
Public Alert Message
        
This is a public alert message to inform you 
that an incident has occurred on {0.date} {0.time} 
in the vicinity of your residential area, 
please follow the advisory stated below on any possible 
follow-up actions.
        
Incident Name: 
{0.name}

Incident Category: 
{0.category}
        
Description:
{0.description}
        
Advisory:
{0.advisory}
"""


class SocialMedia:

    def __init__(self):
        self.alert_authority_renderer = renderer.MessageFormatRenderer(ALERT_AUTHORITY_SPEC)
        self.alert_public_renderer = renderer.MessageFormatRenderer(ALERT_PUBLIC_SPEC)

        self.facebook_connector = connector.FacebookConnector()
        self.sms_connector = connector.SMSConnector()

    def alert_authorities(self, incident: model.Incident, authority):
        self.sms_connector.send_message(self.alert_authority_renderer.render_message(incident),
                                        model.Contact.retrieve_authority_contact(authority).phone)

    def alert_public(self, incident: model.Incident, max_distance_km=5):
        public_members = model.retrieve_nearby_residents(incident, max_distance_km)
        for member in public_members:
            self.sms_connector.send_message(self.alert_public_renderer.render_message(incident), member.phone)

    def post_facebook(self, incident: model.Incident):
        self.facebook_connector.send_message(self.renderer.render_message(incident))


def alert_authorities_test(incident):
    controller = SocialMedia()
    controller.alert_authorities(incident, model.Contact.AUTHORITY_POLICE)


def alert_public_test(incident):
    controller = SocialMedia()
    controller.alert_public(incident)


def post_facebook_test(incident):
    controller = SocialMedia()
    controller.post_facebook(incident)


if __name__ == "__main__":
    incident_obj = model.Incident(0, "Incident 1", "Crisis",
                                  model.GeoCoordinate(1.360320, 103.944397),
                                  "This is a description of the crisis",
                                  "14-Jul-1993", "09:30", "Please do not panic")
    alert_authorities_test(incident_obj)
    #alert_public_test(incident_obj)
    #post_facebook_test(incident_obj)
