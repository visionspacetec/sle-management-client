import openapi_client
from openapi_client.rest import ApiException

host = 'http://localhost:2048/api'
auth = None  # Or use 'BasicAuth'
username = ''
password = ''

command_stop = 'stop-telemetry'
arguments = ['TMUB']
cortex_command_inst = openapi_client.CortexCommandApi()
cortex_command_inst.api_client.configuration.host = host
cortex_command_inst.api_client.configuration.username = username
cortex_command_inst.api_client.configuration.password = password
cortex_stop_command = openapi_client.CortexCommand(command=command_stop, args=arguments)

print('----------Cortex Command API------------')
try:
    print('Getting available Cortex commands...')
    print('Available commands: {}'.format(cortex_command_inst.get_cortex_command_list(authentication=auth)))
except ApiException as e:
    print("Exception when calling CortexCommandApi->get_cortex_command_list: %s\n" % e)
try:
    print('Sending command {} with arguments {}'.format(command_stop, arguments))
    cortex_command_inst.post_cortex_command(cortex_command=cortex_stop_command,
                                            authentication=auth)
    print('Sending the command was successful!')
except ApiException as e:
    print("Exception when calling CortexCommandApi->post_cortex_command: %s\n" % e)
