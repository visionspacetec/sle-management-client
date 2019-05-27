# openapi_client.CortexCommandApi

All URIs are relative to *http://localhost:2048/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cortex_command_list**](CortexCommandApi.md#get_cortex_command_list) | **GET** /cortex-command | Returns a list of the availiable Cortex commands
[**post_cortex_command**](CortexCommandApi.md#post_cortex_command) | **POST** /cortex-command | Send a command to the Cortex


# **get_cortex_command_list**
> list[str] get_cortex_command_list()

Returns a list of the availiable Cortex commands

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.CortexCommandApi()

try:
    # Returns a list of the availiable Cortex commands
    api_response = api_instance.get_cortex_command_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CortexCommandApi->get_cortex_command_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cortex_command**
> post_cortex_command(cortex_command=cortex_command)

Send a command to the Cortex

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.CortexCommandApi()
cortex_command = openapi_client.CortexCommand() # CortexCommand |  (optional)

try:
    # Send a command to the Cortex
    api_instance.post_cortex_command(cortex_command=cortex_command)
except ApiException as e:
    print("Exception when calling CortexCommandApi->post_cortex_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cortex_command** | [**CortexCommand**](CortexCommand.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

