pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'cha0sking/proyecto-final-qualentum'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -f Dockerfile.prod -t %DOCKER_IMAGE%:%DOCKER_TAG% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm --entrypoint sh -v %CD%/tests:/app/tests -v %CD%/dev-requirements.txt:/app/dev-requirements.txt %DOCKER_IMAGE%:%DOCKER_TAG% -c "pip install -r dev-requirements.txt && pytest --cov=app && flake8 app/"'
            }
        }

        stage('Push') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat 'docker push %DOCKER_IMAGE%:%DOCKER_TAG%'
                    bat 'docker tag %DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_IMAGE%:latest'
                    bat 'docker push %DOCKER_IMAGE%:latest'
                }
            }
        }
    }

    post {
        always {
            bat 'docker logout || exit 0'
            bat 'docker rmi %DOCKER_IMAGE%:%DOCKER_TAG% || exit 0'
        }
    }
}