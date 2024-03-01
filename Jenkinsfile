pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'feature-branch']], userRemoteConfigs: [[url: 'https://github.com/prpil/mytest.git']]])
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests -p "*test.py"'
            }
        }
    }
}
