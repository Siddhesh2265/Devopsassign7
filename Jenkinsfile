pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }
        stage('Build') {
            steps {
                bat 'python -m py_compile app.py test_app.py'
                bat 'python app.py'
            }
        }
        stage('Test') {
            steps {
                bat 'python test_app.py'
            }
        }
    }
}
