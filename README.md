
# 1. Python script that accepts a list of URLs to be downloaded

To use de downloader Python 3 script you can execute the following command:

```
python ./Downloader.py http://speedtest.tele2.net/100MB.zip http://de.releases.ubuntu.com/12.04/ubuntu-12.04.5-desktop-i386.iso s3://glovo-public/systems-engineer-interview-1.0-SNAPSHOT.jar
```

If you're on Windows machine, use the PyRun.bat file.

# 2. CloudFormation template and supporting scripts to deploy a basic Java web application

I've choose to use Docker on Amazon ECS using AWS CloudFormation & CLI.

Basically, we will create and run docker container on Amazon ECS using CloudFormation and CLI.

- Containerize a simple Spring boot application
- Use AWS CLI to create Amazon ECR repository
- Build docker image and push to ECR
- CloudFormation stack to create VPC, Subnets, InternetGateway etc
- CloudFormation stack to create IAM role
- CloudFormation stack to create ECS Cluster, Loadbalancer & Listener, Security groups etc
- CloudFormation stack to deploy docker container

## Terminal Window Logs

### Codefrom Git

```
mkdir ~/project
git clone https://github.com/vmoll/aws-cloudformation-docker-ecs.git
cd aws-cloudformation-docker-ecs
```

### Dockerize a simple app

```
# Run on local
docker build -t spring-boot-demo ./app/
docker run -it -p 5000:8080 --rm spring-boot-demo:latest
open http://localhost:8080/
```

### Push Docker Image to ECR on AWS

```
aws ecr create-repository --repository-name spring-boot-demo
aws ecr get-login --no-include-email | sh
IMAGE_REPO=$(aws ecr describe-repositories --repository-names books-api --query 'repositories[0].repositoryUri' --output text)
docker tag spring-boot-demo:latest $IMAGE_REPO:v1
docker push $IMAGE_REPO:v1
```

# Login 

We have also to login to the ECR 

```
aws ecr get-login --no-include-email | sh

aws ecr get-login --region us-east-1
```

This command will return something like this, so type this to login.

```
docker login -u AWS -p
eyJwYXlsb2FkIjoiTzhQYm1CbkF2RDBpVHN4KzJWUlRTcEZwUzhBS3NoVFhRQzVIV2JqUnZzVTRVN2t5ZW1JcnUwbCtyL3NxczUxZXpjVDFPZStGVWRpRGR1Rkxka1Uyemk1ODI2MTB1dnU2dDZpRnpSY3BRaDVuK293c3EwYUJweFgzOW1vcEMwbWVsaWx0S0pidTNlaThvTUJYNEtwT01aM2cwcGxlMGRmcTYrLzdrcjh0Q2puczNDU2ZOdWc2UGtZY3RZcGp5VWYzWHd2Uy9wb1JpZVlJMisvTHhXQ3NLZ0hpV055NDVUOFhwNjZ4cU5RVDArT0dwdmZ1Z3o2dEdFcmRDcDUzd3pjUGoveGJnZUh5VFJGVUhYazBteWdrbS9CSER3eElZSTRMaE9HaTd5VFRvY3c4UHRFaEQzeVlsVVc2eWgycWloTy9JRjlKbzh5NW9tN05ydkZJRW1uZkhMZlJlcHNhaWptYnVVRTh1YXBHZ29QQ3UxeEdOZGZkTXIxT0FHaENWYWlVZ3VPciswMUlwb3pveVk2MjhPMGpIa1ZETmJpYlpacm9Teng1S01rWTVwbmcxaFlCbGgrWUs5dVdHM3lQeWtlY28vZ3UxakQzcCtCNVNVWHBKUmdJcG5ERGdDdE9XTDdtc1Rwd1RubEM1MlkrSm5WNGo1MEpyK0lsc1k2QTdXem9EdHkyYUhzRUNTaGNMLzhKd2thQjRlOFRZSnZhRkE3SVZ0L1FGVk9uNG9lNFpwcjk1Qno4eitCWU9hY1RLRlBJTEhiZUo1eFF1WE1XL1pvbXpkQWMzRnZHeGdLZUNqSVV5T240djVXL091aVhFRnlKUGNzTEJSWXpPM1dIUVduZnBqOFJ6SEEzSjcyZVRpWnVIcEg5eGwxVjBCUG84MHN4RkVjUFp3TWEyaTdneGVldUh5bHFBV3I5R1lWTTN3UjFWbWIzNFdkbXNDK3phc0RPTDdlWGYwcDdMbnR3QUpRYnE0eEhxSm40aVJkWUhHaTlMeUdEU1BoOW1jdzVTei9jN2NOYm9Xdmtic2dkdFN0Y0I5RitIOW94dGc1eUxFdHZ6TGY0NU1BazRiOHN0OFhvRTNUaEt1Q0grSFBDaWNPeUcyWFZ6UDVvSUNZd0pFakkyRCtmc1RnQmpYN0JrcGZpbm90Uk9TV3VlT2luam5tdFlCK3NHL3RONTNJWGFUaEpWWEdFRjh1YmdwOWplQ0xJQXc3dlErR1l4bGhHOVFFdDBtc2RYd2F6VmVNdEM0ZlpVRXRObCtRb2xkR2trTVhqMDFWbGY5cWJielllcS9wWHEyUkp0WE1PRUtTaFBhV1daV241ektSRzdaUFlIejc6YXFWRE1TSk52RmxiVXRsUTBIUEJyOHdOWFJ0TDNpOXJWbDVMNGZMdVpvKytvSWlQUTRBRnhhWG5wUTE1WlpYaTdNYmtjeGJCa2VXL0ltUGVZWlNLS0NJOFFpUVlUMVRRaklYUFRWcXFyK2FTdUF5RmVwdWZnRktCbVp2eWtnPT0iLCJkYXRha2V5IjoiQVFFQkFIaHdtMFlhSVNKZVJ0Sm01bjFHNnVxZWVrWHVvWFhQZTVVRmNlOVJxOC8xNHdBQUFINHdmQVlKS29aSWh2Y05BUWNHb0c4d2JRSUJBREJvQmdrcWhraUc5dzBCQndFd0hnWUpZSVpJQVdVREJBRXVNQkVFREVucmNSY3J0QWZ5MXAzcDdBSUJFSUE3YjRWZTBtOVZ3OVlnR2ExenJ4NDhnQjBENGZHV0dOQzFoZjB1amNpYjFqbXlXU3Z6VHpKMGMxWTVhaitSekV4cFhuT0k2UjF2cHhIRFhKYz0iLCJ2ZXJzaW9uIjoiMiIsInR5cGUiOiJEQVRBX0tFWSIsImV4cGlyYXRpb24iOjE1NTE0MDU5MDB9 https://422259363882.dkr.ecr.us-east-1.amazonaws.com

```

## Let's get the repositoryUri, and Push image to repositoryon ECR
Now we have to discovery the URI to be able to PUSH our image to the ECR on AWS.

```
aws ecr describe-repositories --repository-name spring-boot-demo

docker tag spring-boot-demo 422259363882.dkr.ecr.us-east-1.amazonaws.com/spring-boot-demo:v1

docker push 422259363882.dkr.ecr.us-east-1.amazonaws.com/spring-boot-demo:v1
```

# Create CloudFormation Stacks

Create Cloud formation Stack to define VPC, Subnets using infra directory templates

An overview of the following steps is something like this:

```
aws cloudformation create-stack --template-body file://$PWD/infra/vpc.yml --stack-name vpc

aws cloudformation create-stack --template-body file://$PWD/infra/iam.yml --stack-name iam --capabilities CAPABILITY_IAM

aws cloudformation create-stack --template-body file://$PWD/infra/app-cluster.yml --stack-name app-cluster

# Edit the api.yml to update Image tag/URL under Task > ContainerDefinitions and,
aws cloudformation create-stack --template-body file://$PWD/infra/api.yml --stack-name api
```
Let's start by execute the following comand on AWS CLI console:

```
aws cloudformation create-stack --stack-name vpc --template-body file://$PWD/infra/vpc.yml 
```

Or by doing this way:

```
cd infra
aws cloudformation create-stack --stack-name vpc --template-body file://vpc.yml
```

# Create New User Policy to allow create Roles 
We have also to be sure about the arn policies:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1482712489000",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:PutRolePolicy",
                "lambda:CreateFunction",
                "lambda:InvokeAsync",
                "lambda:InvokeFunction",
                "iam:PassRole",
                "lambda:UpdateAlias",
                "lambda:CreateAlias",
                "lambda:GetFunctionConfiguration",
                "lambda:AddPermission",
                "lambda:UpdateFunctionCode"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

# Create IAM Roles to allow cloudwatch logs
```
aws cloudformation create-stack --stack-name iam --template-body file://%cd%/iam.yml --capabilities CAPABILITY_IAM
```
# Create ECS Cluster, Application Loadbalancer, CloudWatch Log Group, and security Groups

```
aws cloudformation create-stack --stack-name app-cluster --template-body file://%cd%/app-cluster.yml
```

Also if you need to delete or recreate some stack:

```
aws cloudformation delete-stack --stack-name app-cluster
```

# Let's chech the name of images

```
aws ecr describe-repositories
```

# Create New Policy, for Linked Services to the User
Since i was using FARGATE, I had to apply the following policies to the user:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole",
        "iam:PutRolePolicy"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "ecs.amazonaws.com"}}
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeAccountAttributes"
            ],
            "Resource": "*"
        }
    ]
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ECSTaskManagement",
            "Effect": "Allow",
            "Action": [
                "ec2:AttachNetworkInterface",
                "ec2:CreateNetworkInterface",
                "ec2:CreateNetworkInterfacePermission",
                "ec2:DeleteNetworkInterface",
                "ec2:DeleteNetworkInterfacePermission",
                "ec2:Describe*",
                "ec2:DetachNetworkInterface",
                "elasticloadbalancing:DeregisterInstancesFromLoadBalancer",
                "elasticloadbalancing:DeregisterTargets",
                "elasticloadbalancing:Describe*",
                "elasticloadbalancing:RegisterInstancesWithLoadBalancer",
                "elasticloadbalancing:RegisterTargets",
                "route53:ChangeResourceRecordSets",
                "route53:CreateHealthCheck",
                "route53:DeleteHealthCheck",
                "route53:Get*",
                "route53:List*",
                "route53:UpdateHealthCheck",
                "servicediscovery:DeregisterInstance",
                "servicediscovery:Get*",
                "servicediscovery:List*",
                "servicediscovery:RegisterInstance",
                "servicediscovery:UpdateInstanceCustomHealthStatus"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ECSTagging",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*"
        }
    ]
}
```

# Create API Stack

Our last step would be to create the API/Web server stack.

```
aws iam create-service-linked-role --aws-service-name ecs.amazonaws.com

aws cloudformation create-stack --stack-name api --template-body file://%cd%/api.yml
```


## Need to deploy app changes?

There isn't a cleaner way to deploy application changes (container) with CloudFormation, especially if you prefer the same image tag (eg: latest, green, prod etc). There are a few difference options,

- Use new image tag and pass that as parameter to CF stack (api.yml) to update-stack or deploy. Many don't prefer using new revision number for as tag.
- With CloudFormation, some prefer create-stack & delete-stack to manage zero-downtime blue-green deployments, not specifically for ECS. ECS does part of this but this is an option
- Use ECS-CLI if you like Docker Compose structure to define container services. This is interesting but I am not sure this is really useful.
- A little hack to register a new task definition revision and update the service using CLI. Refer the `./deploy_app.sh` script.

```
# ./deploy_app.sh <CLUSTER NAME> <SERVICE NAME> <TASK FAMILY>
./deploy_app.sh cluster books-service apis
# One executed, ECS Service update will take a few minutes for the new task / container go live
```


## References

Find the resources and references on https://devteds.com