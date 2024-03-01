pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature-branch', credentialsId: 'b698d23c-65e4-48a1-b000-fb2fc410b195', url: 'https://github.com/prpil/mytest.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
