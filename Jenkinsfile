pipeline {
  agent none
  stages {
    stage('Unit Test') {
      agent {
        docker {
          image 'debian:8'
        }
        
      }
      steps {
        sh 'pwd'
      }
    }
  }
}