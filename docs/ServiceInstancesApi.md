# openapi_client.ServiceInstancesApi

All URIs are relative to *http://localhost:2048/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_si**](ServiceInstancesApi.md#delete_si) | **DELETE** /service-instances/{si} | Deletes a service instance by name
[**delete_si_list**](ServiceInstancesApi.md#delete_si_list) | **DELETE** /service-instances | Deletes all loaded service instances
[**get_si**](ServiceInstancesApi.md#get_si) | **GET** /service-instances/{si} | Find service instance by name
[**get_si_list**](ServiceInstancesApi.md#get_si_list) | **GET** /service-instances | Get a list of the loaded service instances
[**patch_si**](ServiceInstancesApi.md#patch_si) | **PATCH** /service-instances/{si} | Updates one or more service instance parameters
[**post_si**](ServiceInstancesApi.md#post_si) | **POST** /service-instances/{si} | Adds a service instance


# **delete_si**
> delete_si(si)

Deletes a service instance by name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ServiceInstancesApi()
si = 'si_example' # str | Service instance to delete

try:
    # Deletes a service instance by name
    api_instance.delete_si(si)
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->delete_si: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **si** | **str**| Service instance to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_si_list**
> delete_si_list()

Deletes all loaded service instances

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ServiceInstancesApi()

try:
    # Deletes all loaded service instances
    api_instance.delete_si_list()
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->delete_si_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_si**
> ServiceInstance get_si(si)

Find service instance by name

Returns a single service instance

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ServiceInstancesApi()
si = 'si_example' # str | Service instance identifier

try:
    # Find service instance by name
    api_response = api_instance.get_si(si)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->get_si: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **si** | **str**| Service instance identifier | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_si_list**
> list[str] get_si_list()

Get a list of the loaded service instances

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ServiceInstancesApi()

try:
    # Get a list of the loaded service instances
    api_response = api_instance.get_si_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->get_si_list: %s\n" % e)
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

# **patch_si**
> patch_si(si, request_body=request_body)

Updates one or more service instance parameters

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ServiceInstancesApi()
si = 'si_example' # str | Service instance that needs to be updated
request_body = {'key': openapi_client.SleConfigParamsValues()} # dict(str, SleConfigParamsValues) |  (optional)

try:
    # Updates one or more service instance parameters
    api_instance.patch_si(si, request_body=request_body)
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->patch_si: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **si** | **str**| Service instance that needs to be updated | 
 **request_body** | [**dict(str, SleConfigParamsValues)**](SleConfigParamsValues.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_si**
> post_si(si, service_instance=service_instance)

Adds a service instance

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ServiceInstancesApi()
si = 'si_example' # str | New service instance identifier
service_instance = openapi_client.ServiceInstance() # ServiceInstance |  (optional)

try:
    # Adds a service instance
    api_instance.post_si(si, service_instance=service_instance)
except ApiException as e:
    print("Exception when calling ServiceInstancesApi->post_si: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **si** | **str**| New service instance identifier | 
 **service_instance** | [**ServiceInstance**](ServiceInstance.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

