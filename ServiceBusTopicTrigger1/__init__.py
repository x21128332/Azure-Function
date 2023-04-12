import logging
import json
import azure.functions as func
import requests

def main(message: func.ServiceBusMessage):
    
    # Log the Service Bus Message as plaintext
    message_content_type = message.content_type
    message_body = message.get_body().decode("utf-8")

    logging.info("Python ServiceBus topic trigger processed message.")
    logging.info("Message Content Type: " + message_content_type)
    logging.info("Message Body: " + message_body)

    url = f'https://aislingsbustours-bookingapi.azurewebsites.net/update-booking/{json.loads(message_body)["booking_id"]}'
    headers = {'Content-Type': 'application/json'}
    data = message_body
    response = requests.put(url, data=data, headers=headers)
    print(response.text)

