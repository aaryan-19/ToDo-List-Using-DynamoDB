## Deployiing Project on to the AWS Cloud

### **Steps to create table in DynamoDB**
1. Go to the DynamoDB Service in AWS and click on create table
2. Assign Partition key as `entry_date` and sort key as `task_d`
3. Choose the `Customize settings` option in `Table settings`
4. Choose `Table class` as per your needs. I used `DynamoDB Standard` option as TODO project requires frequent access od data.
5. In `Read/Write capacity settings`, I have chosen `Provisioned` option as traffic is known.
6. Click on `create table` option then.

### **Steps to create an instance in ec2**
1. Go to EC2 -> instance in AWS cloud
2. Click on `Launch Instance`
3. Type name for name and tags according to your choice
4. Choose the application and OS images as per your preference. I chose Ubuntu
5. Choose instance type
6. create or use your existing key-pair
7. On the network settings, configure the security group to control the traffic. And edit the `inbound rules` to allow traffic from your `IP` and change `port number` to `8000`
8. Configure Storage
9. Click on launch instance

### **Steps to connect to instance**
1. Select your instance and click on `Connect`
2. Open the gitbash in your device and copy paste the command which appears when clicked on `Connect`
3. After connection clone the project repository.
3. Install the requirements as mentioned in mysite/README.md
4. Copy public host IP and go to mysite/mysite/settings.py and paste the IP in `allowed_host` list
5. Move to mysite/ directory and run the following command to run the project - `python3 manage.py runserver 0:8000`

`NOTE - Follow the steps mentioned in mysite/README.md to run the project in your instance`