# TASK 10.1 
I install ansible on my virtual box (my virtualbox will be the managing host)
I create the file `inventory.txt`and add names or ip instances to it.
I create a **playbook** that will installed the Apache by `apache.yml file` - **this is my first playbook**
<img src="screenshots/1.png">
<img src="screenshots/2.png">

I run apache.yml playbook.
<img src="screenshots/3.png">
<img src="screenshots/4.png">
Successfully! installed Apache on 2 instances in one click :)

Use a test module `ping/pong` to test
<img src="screenshots/5.png">

Remove apache: change in playbook 
```
state: latest на state: absent
```
<img src="screenshots/6.png">
<img src="screenshots/7.png">

I install the Apache and run Apache and put it on startup, to manage systemd there is a module in ansible, I use it. I add a second task that calls the systemd module and I use three attributes of this module:
- `name` - the name of the systemd service
- `state` - the desired state of the service
- `enabled` - whether it is necessary to register the service in startup
**this is my second playbook**
<img src="screenshots/8.png">
<img src="screenshots/9.png">
<img src="screenshots/10.png">

I make a playbook that creates two users `alex` and `katya` with
key-based authentication and which will have full root permissions via sudo like
and user ec2-user - **this is my third playbook**

Decomposition: 

Just create users. For this I use the module `user`. Create `users.yml file`
<img src="screenshots/11.png">
<img src="screenshots/12.png">
<img src="screenshots/13.png">


Create keys for my users. For each user i need to put his public key in `/ authorized_keys` on all my instances. To make it by ansible, i need the module `authorized_key` and new version of `users.yml`
<img src="screenshots/14.png">
<img src="screenshots/15.png">
<img src="screenshots/16.png">
<img src="screenshots/17.png">

It remains to give these users their private keys and they can go to instances. It is necessary to give users sudo. To do this, I create group - `admin` and add users there. Then I will give this group full rights.

Create group `admin`. For this I use the module `group` and new version of `users.yml file`
<img src="screenshots/18.png">
<img src="screenshots/19.png">
<img src="screenshots/20.png">

Give full rights to the admins group in sudo. There is no module for working with sudo in ansible. If you google how to change the sudo configuration by ansible then one of the ways you can find it is using the modul `lineinfile`. It allows you to add/remove a line in a file. And I need to add the line to the end of the /etc/sudoers. Also new version of `users.yml file` again
<img src="screenshots/20.png">
<img src="screenshots/21.png">

Run and check if my users have full rights
<img src="screenshots/22.png">
<img src="screenshots/23.png">
