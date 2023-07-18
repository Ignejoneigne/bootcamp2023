# sgt-ansible-2023 day 2 lab

## Prerequisites
- Your Git with public repo && Use faculty repo for materials [https://github.com/achenlv/sgt-ansible-2023/]
- Infrastructure on AWS

## Tasks
- Create playbook to get Ansible versions (ansible, playbook, galaxy) and build on Jenkins agent.
- Update playbook to have hosts as parameter variable.
- Make sure that all your servers have latest Java dns library.
- Put Gradle binary in backend server, and get gradle version.
- Use ‘where’ condition for task to combine playbooks 4 and 5.
- Configure nginx on frontend server.

## Useful links
-  https://repo1.maven.org/maven2/dnsjava/dnsjava/3.5.2/
- https://services.gradle.org/distributions/

## Useful commands
- ```ansible-playbook playbook.yaml [--extra-vars var1=value1] [--private-key private.key]```
- ```ansible-galaxy collection install -r requirements.yaml```

## Infrastructure
![image](https://github.com/achenlv/sgt-ansible-2023/assets/48532727/ccafb42f-f0ec-489a-9d1c-2ba07cff3a77)
