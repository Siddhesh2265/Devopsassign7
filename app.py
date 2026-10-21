def greet():
    return "Hello from Jenkins CI!"

if __name__ == "__main__":
    print(greet())



from app import greet

def test_greet():
    assert greet() == "Hello from Jenkins CI!"
    print("All tests passed!")

if __name__ == "__main__":
    test_greet()



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
                dir('Assignment_No.7') {
                    sh 'python3 -m py_compile app.py test_app.py'
                    sh 'python3 app.py'
                }
            }
        }
        stage('Test') {
            steps {
                dir('Assignment_No.7') {
                    sh 'python3 test_app.py'
                }
            }
        }
    }
}
