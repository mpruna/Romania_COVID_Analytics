### Gogs setup

Gogs, an open-source, lightweight Git server. Gogs can be used for small organizations to setup code repository and create pipelines before pushing the code into production.

Gogs can work be installed as a local application or as a containerized application with docker. Gogs require a Backend DB.

### Local install steps

### Debian/Ubuntu

```
sudo apt-get update
sudo apt-get install git
```

### Install from binary

* https://gogs.io/docs/installation/install_from_binary

For example:

```
wget https://dl.gogs.io/0.11.91/gogs_0.11.91_linux_amd64.tar.gz 
tar -xvzf gogs_0.11.91_linux_amd64.tar.gz
```

1. cd into the directory that was just created.
2. Execute ./gogs web.

References:
* https://gogs.io/docs/installation/install_from_binary
* https://gogs.io/docs/installation/install_from_source

Install from source

### Set Up the Environment

```
sudo adduser --disabled-login --gecos 'Gogs' git
```

### Compile Gogs

```
# Clone the repository to the "gogs" subdirectory
git clone --depth 1 https://github.com/gogs/gogs.git gogs
# Change working directory
cd gogs
# Compile the main program, dependencies will be downloaded at this step
go build -o gogs
```

Cd into the directory and execute:

```
./gogs web
``` 

### Setup ssh

It's possible to use ssh keys for git worflows(pull/push etc). The key pair is generated locally. The public key is uploaded to the Gogs server.

There are some extra steps:

* remote url must be setup in ssh format:

* remote url must be setup in ssh format:
  ```git remote set-url origin root@localhost:gogs/COVID_Public.git```
* upstream branch must be setup explicitly:
  ```git push --set-upstream origin master```
  ```
     git push
     fatal: The current branch master has no upstream branch.
     To push the current branch and set the remote as upstream, use
     git push --set-upstream origin master
  ```
* local ssh service must be started:
  
   ```
      ssh -i .ssh/id_rsa  localhost:22
      ssh: Could not resolve hostname localhost:22: Name or service not known
      
      ssh -i .ssh/id_rsa  localhost
      The authenticity of host 'localhost (::1)' can't be established.
      ECDSA key fingerprint is SHA256:a0toXFLJaL/JKaGZA9A+r5/MKoK1udiikzEd4mqQEvE.
      Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
      Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.
      PTY allocation request failed on channel 0
      Hi there, You've successfully authenticated, but Gogs does not provide shell access.
      If this is unexpected, please log in with password and setup Gogs under another user.
      Connection to localhost closed.
    ```




### DB Setup for gogs

1. Create a mysql user

```
CREATE USER 'gogs'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON gogs. * TO 'gogs'@'localhost';
FLUSH PRIVILEGES;
```
Ref:
https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql
