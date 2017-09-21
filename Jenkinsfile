pipeline {
  agent any
  stages {
    stage('Unit Test') {
      steps {
        dockerNode(image: 'python:2.7.14')
      }
    }
  }
}