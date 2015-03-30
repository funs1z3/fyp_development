#!/usr/bin/python
#Author: Sophie Renshaw 20052994
#Date: 30/03/2015
#Sample solution for the Nova Lab Exercise

from os import environ as env
from keystoneclient.v2_0 import client
keystone = client.Client(auth_url=env['OS_AUTH_URL'],#keystone service endpoint for authorisation
			username=env['OS_USERNAME'], #username for auth
			password=env['OS_PASSWORD'], #password for auth
			tenant_name=env['OS_TENANT_NAME']) #tenant name

print keystone.auth_token
