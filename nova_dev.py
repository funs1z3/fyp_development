#!/usr/bin/python
#Author: Sophie Renshaw 20052994
#Date: 30/03/2015
#Sample solution for the Nova Lab Exercise

from os import environ as env
from keystoneclient.v2_0 import client
import glanceclient.v2.client as glclient
#from credentials import get_nova_credentials_v2
from novaclient.client import Client
keystone = client.Client(auth_url=env['OS_AUTH_URL'],#keystone service endpoint for authorisation
			username=env['OS_USERNAME'], #username for auth
			password=env['OS_PASSWORD'], #password for auth
			tenant_name=env['OS_TENANT_NAME']) #tenant name

#print keystone.auth_token
glance_endpoint = keystone.service_catalog.url_for(service_type ='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
images = glance.images.list()
print list(images)

def get_nova_credentials_v2():
	d = {}
	d['version'] = '2'
	d['username'] = env['OS_USERNAME']
	d['api_key'] = env['OS_PASSWORD']
	d['auth_url'] = env['OS_AUTH_URL']
	d['project_id'] = env['OS_TENANT_NAME']
	return d

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

print(nova_client.servers.list())

image = nova_client.images.find(name="phusion/baseimage")
flavor = nova_client.flavors.find(name="m1.tiny")
net = nova_client.networks.find(label="private")

nics = [{'net-id': net.id}]
instance = nova_client.servers.create(name="container1", image=image, flavor=flavor, nics=nics)
print("VMs:")
print(nova_client.servers.list())
