# fyp_development
##Step 1:Hardware Configuration 
* Ensure that the essential hardware is available. This includes two Raspberry Pi’s and relevant SD cards and power cables as well as either a switch/router and ethernet cables or wireless adapters.
* Download the Raspbian image from raspberrypi.org/downloads.
* Insert the SD card into a laptop to copy Raspbian onto it. A program will be needed to write the file to the SD card. Win32Disk can be used for Windows or the dd command can be used with Linux. 
* Once the file has copied the SD card can be removed from the laptop and inserted into the Raspberry Pi. The above step can be repeated for the other SD card.
* Connect the Raspberry Pi to the power and to a router via an ethernet cable (wireless connectivity will be configured later).
* Access the gateway of your router, usually 192.168.1.1 to find the IP address of the Raspberry Pi’s. 
* Access the Pi’s via SSH; either using putty on a Windows machine or the command line for Linux. 
* Run raspi-config to change hostname and expand partition as well as change the amount of RAM allocation to the GPU down to 16MB. 
* Configure your wireless adapter to work with the Pi following the steps that are relevant to your adapter. Edit the etc/network/interfaces to recognise the adapter and set a static IP address on it.

(Raspberry Pi, 2015)
 
##Step 2: Devstack Configuration
* Create a new user stack:

	adduser stack
	
*  Give stack sudo privileges: 

	apt-get install sudo -y || yum install -y sudo
	echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
	
* Change to user stack and start the devstack pull and install
	
	sudo apt-get install git -y || sudo yum install -y git
	git clone https://git.openstack.org/openstack-dev/devstack /opt/stack/devstack
	cd devstack

* Configure the local.conf
* Run Devstack

	/stack.sh
	
(Openstack, 2015)

##Step 3: Configure Docker to work with Devstack
This step is only currently available on a Ubuntu distribution. Nova-docker has not been ported to Debian or Fedora yet.

* Edit local.conf to include:

	VIRT_DRIVER=docker

* Download the nova-docker packages

	git clone https://git.openstack.org/stackforge/nova-docker /opt/stack/nova-docker

* Configure Devstack

	cd /opt/stack/nova-docker
	./contrib/devstack/prepare_devstack.sh

* Re-run stack.sh

	./stack.sh

(Openstack Wiki, 2015)

##Step 4: Error Troubleshooting
When configuring on a Raspberry Pi stack.sh will come across issues while installing Devstack. These may include package errors, networking issues, resource issues etc. To help resolve these errors and issues see Issues Section.

##Step 5: Using Docker with Devstack
* Return the glance image list to show any docker images. Only docker images will be bootable as a linux container.

	glance image-list

* Fetch docker image from public registry

	docker search debian

* Add this docker image to glance

	docker pull debian	
	docker save debian | glance image-create --is-public=True /
	--container-format=docker --disk-format=raw --name debian

* Returning the glance image list shows the docker image
	
	glance image-list	

* Boot a nova instance using the CLI and the docker image that was just downloaded.

	nova boot --image “debian” --flavor m1.tiny test

(Openstack Wiki, 2015)

##Step 6: Using the Test Script.

Once the student has created their script and saved as nova_solution.py in the same directory that test_dev.py and nova_dev.py is saved they can run the test_dev.py file:

	python test_dev.py
	
This will return a percentage to the student.
