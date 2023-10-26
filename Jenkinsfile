pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                // Clona tu repositorio de GitHub
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas Unitarias') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Análisis de Calidad del Código') {
            steps {
                withSonarQubeEnv('SonarQube Server') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Construir y Subir a Docker Hub') {
            steps {
                // Construir la imagen de Docker
                sh 'docker build -t docker_img.'
                
                // Autenticarse en Docker Hub (reemplaza 'tu_usuario' y 'tu_contraseña' con tus credenciales)
                sh 'docker login -u tu_usuario -p tu_contraseña'

                // Subir la imagen a Docker Hub (reemplaza 'nombre_de_tu_usuario' y 'nombre_de_tu_imagen' con tu información)
                sh 'docker push nombre_de_tu_usuario/nombre_de_tu_imagen'
            }
        }
    }

    post {
        failure {
            // Manejar acciones en caso de fallos en alguna etapa
            mail to: 'estherochoagonzalez@gmail.com',
                 subject: 'Fallo en el Pipeline de Jenkins',
                 body: "El pipeline de Jenkins ha fallado en una de las etapas."
        }
    }
}
