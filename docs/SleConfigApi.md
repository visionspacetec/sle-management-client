# openapi_client.SleConfigApi

All URIs are relative to *http://localhost:2048/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sle_config**](SleConfigApi.md#get_sle_config) | **GET** /sle-config/{param} | Returns the current value of a SLE configuration parameter
[**get_sle_config_list**](SleConfigApi.md#get_sle_config_list) | **GET** /sle-config | Get a list of the available configuration parameters
[**patch_sle_config**](SleConfigApi.md#patch_sle_config) | **PATCH** /sle-config/{param} | Update a SLE configuration parameter


# **get_sle_config**
> SleConfigParamsValues get_sle_config(param)

Returns the current value of a SLE configuration parameter

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SleConfigApi()
param = openapi_client.SleConfigParams() # SleConfigParams | Name of the parameter to return

try:
    # Returns the current value of a SLE configuration parameter
    api_response = api_instance.get_sle_config(param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SleConfigApi->get_sle_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param** | [**SleConfigParams**](.md)| Name of the parameter to return | 

### Return type

[**SleConfigParamsValues**](SleConfigParamsValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sle_config_list**
> list[SleConfigParams] get_sle_config_list()

Get a list of the available configuration parameters

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SleConfigApi()

try:
    # Get a list of the available configuration parameters
    api_response = api_instance.get_sle_config_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SleConfigApi->get_sle_config_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SleConfigParams]**](SleConfigParams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sle_config**
> patch_sle_config(param, sle_config_params_values=sle_config_params_values)

Update a SLE configuration parameter

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.SleConfigApi()
param = openapi_client.SleConfigParams() # SleConfigParams | Name of the parameter that needs to be updated
sle_config_params_values = openapi_client.SleConfigParamsValues() # SleConfigParamsValues |  (optional)

try:
    # Update a SLE configuration parameter
    api_instance.patch_sle_config(param, sle_config_params_values=sle_config_params_values)
except ApiException as e:
    print("Exception when calling SleConfigApi->patch_sle_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **param** | [**SleConfigParams**](.md)| Name of the parameter that needs to be updated | 
 **sle_config_params_values** | [**SleConfigParamsValues**](SleConfigParamsValues.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

