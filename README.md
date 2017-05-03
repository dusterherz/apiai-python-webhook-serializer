# Apiai Python Webhook Serializer

[![PyPI version](https://badge.fury.io/py/apiaiWebhookSerializer.svg)](https://badge.fury.io/py/apiaiWebhookSerializer)

Convert Api.ai webhook requests and responses to a python object with a proper Serializer.

## What is APWS ? And Why ?

Apiai Python Webhook Serializer (APWS) is a little Serializer / Deserializer to translate the JSON recieved and sended from Api.ai. This allows to have proper python objects instead of dictionaries from parsed json and to transform an object into a proper json for Api.ai.

## How does this work ?

APWS is constitued of two classes : Request and Response.

### Request

Request is here to parse recieved JSON from Api.ai and Response to answer the request.
Request take the body from the request at its creation. Then you can access objects like the sessionId writing `request.sessionId`.
You can find all the fields that you can use [here](https://docs.api.ai/docs/query#response).

### Response

Reponse is here to create a python object that can be return like that for example with flask.
Response take multiples informations for its creation. Three are mandatory : `speech`, `displayText` and `source`. Three others are optional : `data`, `contextOut` and `followupEvent`.
You can find more details on this [here](https://docs.api.ai/docs/webhook#section-format-of-response-from-the-service)
With Response you can also format it into a dictionary with the method `format()` if you are not using Flask.
This class integrate also an error formater method for Api.ai (`error`). This method takes two parameters : `httpErrorCode` (the http error code corresponding to the error), and `errorMsg` (the message of the error). `error` is static so you can use it without initializing a Response object.

## Examples ?

WIP.

## Installation

You can install APWS via pip : `pip install apiaiWebhookSerializer`

## License

MIT. Read LICENSE file for more information.
