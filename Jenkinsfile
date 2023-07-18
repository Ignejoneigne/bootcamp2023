pipeline {
  agent any

  stages {
    stage('Ansible') {
      steps {
        sh '''#!/usr/bin/env bash
          ansible --version
          ansible-playbook --version
          ansible-galaxy --version
        '''
      }
    }
  }
}
