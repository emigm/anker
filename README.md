# Anker
Anker is the result of a personal initiaciative to start using Ansible and Docker to deploy HTTP Services written in Python.
The current version deploy an Echo HTTP service in a local environment.

# Dependencies

* Ansible: <http://docs.ansible.com/intro_installation.html>
* Docker: <http://docs.docker.com/installation/>

# Usage

Clone the repository and get into the deploy directory.
```
cd anker/deploy
```
Build the Docker images.
```
ansible-playbook -i envs/dev/inventory images.yml
```
Run Docker containers.
```
ansible-playbook -i envs/dev/inventory site.yml
```
Check that the Echo HTTP service is up and running.
```
curl -X POST http://localhost/echo -d "Hello"
```
