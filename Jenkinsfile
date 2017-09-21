pipeline {
  agent {
    docker {
      image 'python:2.7'
    }
    
  }
  stages {
    stage('Print Hello') {
      steps {
        sh 'echo "Hello"'
      }
    }
  }
}