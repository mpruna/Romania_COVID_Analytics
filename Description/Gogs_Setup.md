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

### DB Setup for gogs

1. Create a mysql user

```
CREATE USER 'gogs'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON gogs. * TO 'gogs'@'localhost';
FLUSH PRIVILEGES;
```
Ref:
https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql
