# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.user_schema_api import UserSchemaApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserSchemaApi(unittest.TestCase):
    """UserSchemaApi unit test stubs"""

    def setUp(self):
        self.api = UserSchemaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_application_user_schema(self):
        """Test case for get_application_user_schema

        Fetches the Schema for an App User  # noqa: E501
        """
        pass

    def test_get_user_schema(self):
        """Test case for get_user_schema

        Fetches the schema for a Schema Id.  # noqa: E501
        """
        pass

    def test_update_application_user_profile(self):
        """Test case for update_application_user_profile

        Partial updates on the User Profile properties of the Application User Schema.  # noqa: E501
        """
        pass

    def test_update_user_profile(self):
        """Test case for update_user_profile

        """
        pass


if __name__ == '__main__':
    unittest.main()