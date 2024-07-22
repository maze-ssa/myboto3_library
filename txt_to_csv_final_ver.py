import boto3
import csv

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'patchupdatebucket19072024'
    input_prefix = 'raw/'
    output_prefix = 'result/'

    # Get the list of objects in the input prefix
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=input_prefix)

    # Process each object
    for obj in objects['Contents']:
        key = obj['Key']
        if key.endswith('/'):  # Skip directories
            continue
        file_name = key.split('/')[-1]

        # Read the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=key)
        file_content = response['Body'].read().decode('utf-8')

        # Parse the file content
        rows = []
        instance_id = 'i-0e38320c944ca2216'  # Assuming instance ID
        for line in file_content.splitlines():
            columns = line.split()  # Split by any whitespace
            if len(columns) >= 3:  # Check if there are at least 3 columns
                columns[0] = instance_id  # Replace the first column with the instance ID
                rows.append(columns)

        # Add the header row
        rows.insert(0, ['Name', 'PackageName', 'AvailabeVersion', 'Repository'])

        # Write the output to a new file
        output_file_name = file_name + '.csv'  # Add .csv extension
        with open('/tmp/output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        # Upload the output file to S3
        s3.put_object(Body=open('/tmp/output.csv', 'rb'), Bucket=bucket_name, Key=output_prefix + output_file_name)

    return {
        'statusCode': 200,
        'statusMessage': 'OK'
    }