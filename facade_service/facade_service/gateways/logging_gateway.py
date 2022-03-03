from facade_service.gateways.base_gateway import BaseGateway


DEFAULT_LOGGING_ENDPOINT = "/logging-service"


class LoggingGateway(BaseGateway):

    def __init__(self, app=None):
        super(LoggingGateway, self).__init__(app)

    def init_gateway(self, app):
        self.base_path = app.config['LOGGING_SERVICE_GATEWAY']

    def send_message(self, message):
        self._post(
            url=self._build_url(endpoint=DEFAULT_LOGGING_ENDPOINT),
            payload=message
        )

    def get_messages(self):
        response = self._get(
            url=self._build_url(endpoint=DEFAULT_LOGGING_ENDPOINT)
        )
        return response


logging_gateway = LoggingGateway()



