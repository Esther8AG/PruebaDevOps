pipeline {
    agent any 

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t myapp .'
                }
            }
        }
        stage('Test') {
            steps {
                // añadir comandos para ejecutar pruebas
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                //añadir comandos para desplegar tu aplicación
                echo 'Deploying application...'
            }
        }
    }
}
