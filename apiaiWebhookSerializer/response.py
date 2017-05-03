class Response:
    def __init__(self, speech, displayText, source, data={}, contextOut=[], followupEvent={}):
        self.speech = speech
        self.displayText = displayText
        self.data = data
        self.contextOut = contextOut
        self.source = source
        self.followupEvent = followupEvent

    def format(self):
        response = {
            "speech": self.speech,
            "displayText": self.displayText,
            "source": self.source
        }
        if self.data:
            response["data"] = self.data
        if self.contextOut:
            response["contextOut"] = self.contextOut
        if self.followupEvent:
            response["followupEvent"] = self.followupEvent
        return response

    def error(httpErrorCode, errorMsg):
        response = {
            "status": {
                "code": httpErrorCode,
                "errorType": errorMsg
            }
        }
        return response
