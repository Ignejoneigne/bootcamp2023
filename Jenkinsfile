pipeline {
  agent any

  parameters {
    string defaultValue: 'all', name: 'Hosts'

  }
  environment {
    ANSIBLE_PRIVATE_KEY=credentials('ansible-private-key') 
    HOSTS="${params.Hosts}"
  }
  stages {
    stage('Ansible') {
      steps {
        sh '''#!/usr/bin/env bash
          ansible-playbook -i ${Hosts} --private-key=${ANSIBLE_PRIVATE_KEY} playbooks/task2.yaml
        '''
      }
    }
  }
}
