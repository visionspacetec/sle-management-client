# ServiceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **int** | ToDo - not yet supported | [optional] 
**stop_time** | **int** | ToDo - not yet supported | [optional] 
**initiator_id** | **str** |  | [optional] [default to 'SLE_USER']
**responder_id** | **str** |  | [optional] [default to 'SLE_PROVIDER']
**return_timeout_period** | **int** |  | [optional] [default to 15]
**delivery_mode** | **str** | ToDo - Only timely online supported | [optional] [default to 'TIMELY_ONLINE']
**initiator** | **str** |  | [optional] [default to 'USER']
**permitted_frame_quality** | **list[str]** |  | [optional] [default to ["allFrames"]]
**latency_limit** | **int** |  | [optional] [default to 9]
**transfer_buffer_size** | **int** |  | [optional] [default to 1]
**report_cycle** | **int** |  | [optional] 
**requested_frame_quality** | **str** |  | [optional] [default to 'allFrames']
**state** | **str** |  | [optional] [default to 'unbound']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


