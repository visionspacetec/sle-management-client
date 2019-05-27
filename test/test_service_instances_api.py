# coding: utf-8

"""
    sle-management-client

    Python SLE Provider Management Client

    OpenAPI spec version: 0.1.0
    Contact: oss@visionspace.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.service_instances_api import ServiceInstancesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestServiceInstancesApi(unittest.TestCase):
    """ServiceInstancesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.service_instances_api.ServiceInstancesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_si(self):
        """Test case for delete_si

        Deletes a service instance by name  # noqa: E501
        """
        pass

    def test_delete_si_list(self):
        """Test case for delete_si_list

        Deletes all loaded service instances  # noqa: E501
        """
        pass

    def test_get_si(self):
        """Test case for get_si

        Find service instance by name  # noqa: E501
        """
        pass

    def test_get_si_list(self):
        """Test case for get_si_list

        Get a list of the loaded service instances  # noqa: E501
        """
        pass

    def test_patch_si(self):
        """Test case for patch_si

        Updates one or more service instance parameters  # noqa: E501
        """
        pass

    def test_post_si(self):
        """Test case for post_si

        Adds a service instance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()