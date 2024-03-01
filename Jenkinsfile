pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature branch', url: 'https://github.com/prpil/mytest.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests -p "*test.py"'
            }
        }
    }
}
