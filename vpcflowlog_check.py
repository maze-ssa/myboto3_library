import boto3

def check_vpc_flow_log_enabled(vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.describe_flow_logs(
        Filter=[
            {
                'Name': 'esource-id',
                'Values': [vpc_id]
            }
        ]
    )
    if response['FlowLogs']:
        return True
    else:
        return False

vpc_id = 'your_vpc_id'  # Replace with your VPC ID
if check_vpc_flow_log_enabled(vpc_id):
    print(f"VPC flow log is enabled for VPC {vpc_id}")
else:
    print(f"VPC flow log is not enabled for VPC {vpc_id}")