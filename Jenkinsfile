pipeline {
  agent none
  stages {
    stage('Unit Test') {
      agent {
        docker {
          image 'python:2.7'
        }
        
      }
      steps {
        sh 'pip install pytest'
        sh 'py.test tests'
      }
    }
  }
}