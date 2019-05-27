# openapi_client.CortexConfigApi

All URIs are relative to *http://localhost:2048/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cortex_config_table**](CortexConfigApi.md#get_cortex_config_table) | **GET** /cortex-config/{param} | Returns the parameter names of a Cortex configuration table
[**get_cortex_config_table_list**](CortexConfigApi.md#get_cortex_config_table_list) | **GET** /cortex-config | Get a list of the available configuration tables


# **get_cortex_config_table**
> list[str] get_cortex_config_table(param)

Returns the parameter names of a Cortex configuration table

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.CortexConfigApi()
param = 'param_example' # str | Name of the table to return

try:
    # Returns the parameter names of a Cortex configuration table
    api_response = api_instance.get_cortex_config_table(param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CortexConfigApi->get_cortex_config_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param** | **str**| Name of the table to return | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cortex_config_table_list**
> list[str] get_cortex_config_table_list()

Get a list of the available configuration tables

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.CortexConfigApi()

try:
    # Get a list of the available configuration tables
    api_response = api_instance.get_cortex_config_table_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CortexConfigApi->get_cortex_config_table_list: %s\n" % e)
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

