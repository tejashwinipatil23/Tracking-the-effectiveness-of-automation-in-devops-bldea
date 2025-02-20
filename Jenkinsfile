pipeline {
    agent any
    environment {
        REGISTRY_URL = 'devops-registry.com'
        APP_IMAGE = 'tracking-app'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/devops-tracking.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $REGISTRY_URL/$APP_IMAGE .'
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    sh 'docker push $REGISTRY_URL/$APP_IMAGE'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                    kubectl apply -f k8s/deployment.yaml
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}

