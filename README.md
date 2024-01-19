# MASS EMAILING WITH LAMBDA

## Services
- Lambda
- SES
- IAM
- CloudWatch

## Steps
### 1. Create an IAM role
- Navigate to IAM and search for "Roles" in the side bar.
- Click "Create role"
- Leave Trusted entity type as "AWS service"
- Choose "Lambda" as the service to give permission to Lambda to perform actions in your account.
- Click "Next"
- Add the following permissions:
    - CloudWatch - FullAccess (not V2)
    - SES - FullAccess
- Click "Next"
- Enter role name as "MassEmailingRole"
- Review your configuration
- Click "Create role"

### 2. Create a Lambda Function
- Navigate to Lambda
- Create function
- Leave as "Author from scratch"
- Enter function name as "MassEmailingFunction"
- Choose the latest Python version as Runtime
- Click on "Change default execution role"  dropdown
- Choose "Use an existing role"
- Choose an existing role "MassEmailingRole"
- Create Function

### 3. Configure the Lambda Function

### 4. Create a CloudWatch Event 
- Navigate to CloudWatch > Events > Rules
- Click "Create rule"
- Enter rule name as "MassEmailingRule"
- Choose "Rule type" as "Schedule"
- Click on "Continue to create rule"
- Choose "A schedule that runs at a regular rate, such as every 10 minutes."
- Enter rate as 2 minutes

