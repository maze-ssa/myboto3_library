echo #!/bin/bash
 
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
INSTANCE_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
echo "InstanceName,PackageName,Date,Month,Year" > $(hostname)$(date +'%Y-%m-%d').csv
rpm -qa --last | grep "Aug 2024" | awk -v instance_id="$INSTANCE_ID" '{print instance_id "," $1 "," substr($3,1,2) "," $4 "," $5}' >> $(hostname)$(date +'%Y-%m-%d').csv