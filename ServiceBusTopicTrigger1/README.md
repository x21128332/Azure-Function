# Python ServiceBusTopicTrigger

This is the Function that is pulling data from the service bus and sending it to the API

## Functions
In VSCode, using Azure Tools extension, create a new function app. Pass it the service bus details it asks for.
Move to configuration settings and add an application setting called "aislingsbustoursqueue_SERVICEBUS" with the vaule
being pulled from key vault:
@Microsoft.KeyVault(SecretUri=https://keyvaultabt.vault
.azure.net/secrets/servicebusconnectionstring/) 
Update the keyvault name and secret key name to match your key vault and secret key name.

## Key vault - add identity
In the Azure Key Vault, go to the Access policies and add a  new policy for your funciton. Give both "GET" and "LIST" permissions.
