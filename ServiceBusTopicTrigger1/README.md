# Python ServiceBusTopicTrigger

This is the Function that is pulling data from the service bus and sending it to the API

It should be deployed to Azure Functions.

Once deployed you need to add an application setting under Configuration
Name: `aislingsbustoursqueue_SERVICEBUS`: Value: `<service bus endpoint key>`

You should use keyvault here to hide your key