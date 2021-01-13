#!/usr/bin/env groovy
pipeline {
   agent any
    
   environment {
      VALUE_ONE = '1'
      VALUE_TWO = '2'
      VALUE_THREE = '3'
   }
    
   stages {
   
      // skip a stage while creating the pipeline
      stage("A stage to be skipped") {
         when {
            expression { false }  //skip this stage
         }
         steps {
            echo 'This step will never be run'
         }
      }
      
      // Execute when branch = 'master'
      stage('checkout') {
         when {
            branch 'master'
	 }
         steps {
            checkout scm
         }
      }
      
      // Expression based when example with AND
      stage('WHEN EXPRESSION with AND') {
         when {
            expression {
               VALUE_ONE == '1' && VALUE_THREE == '3'
            }
         }
         steps {
            echo 'WHEN with AND expression works!'
         }
      }
      
      // Expression based when example
      stage('WHEN EXPRESSION with OR') {
         when {
            expression {
               VALUE_ONE == '1' || VALUE_THREE == '2'
            }
         }
         steps {
            echo 'WHEN with OR expression works!'
         }
      }
      
      // When - AllOf Example
      stage("AllOf") {
        when {
            allOf {
                environment name:'VALUE_ONE', value: '1'
                environment name:'VALUE_TWO', value: '2'
            }
        }
        steps {
            echo "AllOf Works!!"
        }
      }
      

   }
}
