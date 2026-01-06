pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'cha0sk1ng/proyecto-final-qualentum'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -f Dockerfile. prod -t %DOCKER_IMAGE%:%DOCKER_TAG% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker build -t test-image .'
                bat 'docker run --rm test-image pytest --cov=app'
                bat 'docker run --rm test-image flake8 app/'
            }
        }

        stage('Push') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push %DOCKER_IMAGE%:%DOCKER_TAG%'
                    bat 'docker tag %DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_IMAGE%: latest'
                    bat 'docker push %DOCKER_IMAGE%: latest'
                }
            }
        }
    }

    post {
        always {
            bat 'docker logout || exit 0'
            bat 'docker rmi %DOCKER_IMAGE%:%DOCKER_TAG% || exit 0'
            bat 'docker rmi test-image || exit 0'
        }
    }
}