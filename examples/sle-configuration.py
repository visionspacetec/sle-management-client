import urllib3
import openapi_client
from openapi_client.rest import ApiException
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

host = 'http://localhost:2048/api'
auth = None  # Or use 'BasicAuth'
username = ''
password = ''

print('----------SLE CONFIG------------')
sle_instance = openapi_client.SleConfigApi()
sle_instance.api_client.configuration.host = host
sle_instance.api_client.configuration.username = username
sle_instance.api_client.configuration.password = password
param = openapi_client.SleConfigParams.AUTHENTICATION_DELAY
sle_config_params_values = 99

try:
    print('Getting: {}...'.format(param))
    print('{}: {}'.format(param, sle_instance.get_sle_config(param,
                                                             authentication=auth)))
except ApiException as e:
    print("Exception when calling SleConfigApi->get_sle_config: %s\n" % e)

try:
    print('Updating: {} to {}...'.format(param, sle_config_params_values))
    sle_instance.patch_sle_config(param,
                                  sle_config_params_values=sle_config_params_values,
                                  authentication=auth)
except ApiException as e:
    print("Exception when calling SleConfigApi->patch_sle_config: %s\n" % e)

try:
    print('Getting: {}...'.format(param))
    print('{}: {}'.format(param, sle_instance.get_sle_config(param,
                                                             authentication=auth)))
except ApiException as e:
    print("Exception when calling SleConfigApi->get_sle_config: %s\n" % e)

print('--------SERVICE INSTANCES-------')
si_instance = openapi_client.ServiceInstancesApi()
si_instance.api_client.configuration.host = host
si_instance.api_client.configuration.username = username
si_instance.api_client.configuration.password = password

try:
    print('Getting service instance list...')
    si_list = si_instance.get_si_list(authentication=auth)
    print(si_list)
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->get_si_list: %s\n" % e)

try:
    si = si_list[0]
    try:
        print('Getting parameters for service instance {}...'.format(si))
        print(si_instance.get_si(si, authentication=auth))
    except ApiException as e:
        print("Exception when calling ServiceInstancesApi->get_si: %s\n" % e)

    try:
        print('Deleting service instance: {}...'.format(si))
        si_instance.delete_si(si, authentication=auth)
    except ApiException as e:
        print("Exception when calling ServiceInstancesApi->delete_si: %s\n" % e)

    try:
        print('Getting service instance list...')
        print(si_instance.get_si_list(authentication=auth))
    except ApiException as e:
        print("Exception when calling ServiceInstancesApi->get_si_list: %s\n" % e)
except Exception as e:
    print('No service instances loaded!')
