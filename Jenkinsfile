pipeline {
  agent {
      docker {
        image 'debian:8'
      }
        
    }
  stages {
    stage('Unit Test') {
      
      steps {
        sh 'apt-get update'
      }
    }
  }
}