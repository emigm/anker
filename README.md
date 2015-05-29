# Anker
Anker is the result of a personal initiaciative to start using Ansible and Docker to deploy HTTP Services written in Python.
The current version deploys an Echo HTTP service in a local environment.

# Dependencies

* Ansible: <http://docs.ansible.com/intro_installation.html>
* Docker: <http://docs.docker.com/installation/>

# Usage

Clone the repository and get into the deploy directory.
```
cd anker/deploy
```
Edit the group_vars/all.yml file and replace the following key values:
```
app_maintainer_email: your.email@gmail.com
app_maintainer_name: Your Name
app_maintainer_username: yourusername
```
Build the Python package.
```
ansible-playbook -i envs/dev/inventory build_py_app.yml
```
Build the Docker images.
```
ansible-playbook -i envs/dev/inventory build_cont_imgs.yml
```
Run Docker containers.
```
ansible-playbook -i envs/dev/inventory run_multi_cont.yml
```
Check that the Echo HTTP service is up and running.
```
curl -X POST http://localhost/echo -d "Hello"
```

NOTE: You can go through all the process by executing just one playbook.
```
ansible-playbook -i envs/dev/inventory site.yml
```
