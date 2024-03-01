pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/prpil/mytest.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests -p "*test.py"'
            }
        }
        stage('Deploy') {
            steps {
                // Execute command on EC2 instance using AWS Systems Manager
                sh 'aws ssm send-command --document-name "AWS-RunShellScript" --targets "Key=instanceids,Values=i-0d631997184b083e0" --parameters "commands=python test.py"'
            }
        }
    }
}
