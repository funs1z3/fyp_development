#!/usr/bin/python
#Author: Sophie Renshaw 20052994
#Date: 30/03/2015
#Sample solution for the Nova Lab Exercise

from os import environ as env
from keystoneclient.v2_0 import client
import glanceclient.v2.client as glclient
#from credentials import get_nova_credentials_v2
from novaclient.client import Client
import os
import time
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

image = nova_client.images.find(name="phusion/passenger-full")
flavor = nova_client.flavors.find(name="m1.tiny")
net = nova_client.networks.find(label="private")

nics = [{'net-id': net.id}]
instance = nova_client.servers.create(name="webserver", image=image, flavor=flavor, nics=nics)
print("VMs:")
print(nova_client.servers.list())
time.sleep(30)
os.system("docker ps")
dockerid = raw_input('Docker ID: ')
os.system("docker exec -t -i " + dockerid + " rm -f /etc/service/nginx/down")
os.system("docker exec -t -i " +  dockerid + " service nginx start")

instance = nova_client.servers.create(name="client", image=image, flavor=flavor, nics=nics)
print("VMs:")
print(nova_client.servers.list())
time.sleep(30)
os.system("docker ps")
dockerid = raw_input('Docker ID: ')
os.system("nova list")
webserverip = raw_input("IP Address: ")
os.system("docker exec -t -i " + dockerid + " wget " + webserverip)


