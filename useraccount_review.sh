echo #!/bin/bash
 
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
INSTANCE_ID=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
result=$(echo "InstanceID,Username,LAST-LOGIN,PWD-CHANGE"; lslogins -u -o USER,LAST-LOGIN,PWD-CHANGE | awk -v instance_id=$INSTANCE_ID 'NR>1{print instance_id","$1","$2","$3}' | sed 's/ */,/g')
echo "$result" > $(hostname)$(date +'%Y-%m-%d').csv