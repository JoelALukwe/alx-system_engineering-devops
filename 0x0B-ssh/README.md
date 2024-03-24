0x0B-ssh


TOPICS COVERED IN THIS PROJECT
1.DEV-OPS
2.SSH
3.NETWORK
4.SYS-ADMIN
5.SECURITY


RESOURCES

1.What is a (physical) server - text (Https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
2.What is a (physical) server - video(https://youtu.be/B1ANfsDyjeA?si=w78bEetYB0oI0s6Q)
3.SSH essentials(https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
4.SSH Config File(https://www.ssh.com/academy/ssh/config)
5.Public Key Authentication for SSH(https://www.ssh.com/academy/ssh/public-key-authentication)
6.How Secure Shell Works(https://youtu.be/ORcvSkgdA58?si=iAsZcodbQev7uLju)
7.SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)
(https://youtu.be/hQWRp-FdTpc?si=DUrGXeChd0QcAa-h)


for refference

1.Understanding the SSH Encryption and Connection Process(https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)

2.Secure Shell Wiki(https://en.wikipedia.org/wiki/Secure_Shell)

3.IETF RFC 4251 (Description of the SSH Protocol)(https://www.ietf.org/rfc/rfc4251.txt)

4.Internet Engineering Task Force(https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)

5.Request for Comments(en.wikipedia.org/wiki/Request_foRequest for Commentsr_Comments)






QUESTIONS ANSWERED 
What is a server
Where servers usually live
What is SSH
How to create an SSH RSA key pair
How to connect to a remote host using an SSH RSA key pair
The advantage of using #!/usr/bin/env bash instead of /bin/bash



REQUIREMENTS FOR THE PROJECT

Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing





TASKS

0. Use a private key
mandatory
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase





1. Create an SSH key pair
mandatory
Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty





2. Client configuration file
mandatory
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password






3. Let me in!
mandatory
Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.



4. Client configuration file (w/ Puppet)
#advanced
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password
