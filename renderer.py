import model


class MessageRenderer:

    def render_message(self, incident: model.Incident) -> str:
        raise NotImplementedError("render_message method not implemented")


class StubMessageRenderer(MessageRenderer):

    def render_message(self, incident: model.Incident) -> str:
        return "Stub message"


class MessageFormatRenderer(MessageRenderer):

    def __init__(self, format_spec: str):
        self.format_spec = format_spec

    def render_message(self, incident: model.Incident) -> str:
        return self.format_spec.format(incident)