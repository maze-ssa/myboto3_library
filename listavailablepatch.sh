echo #!/bin/bash
 
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
INSTANCE_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
echo "InstanceName,PackageName,Version,Repo" > $(hostname)$(date +'%Y-%m-%d').csv
yum list updates | awk -v instance_id=$INSTANCE_ID '{print instance_id "," $1 "," $2 "," $3}' | tail -n +8 >> $(hostname)$(date +'%Y-%m-%d').csv