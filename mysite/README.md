This directory contains the code for the TODO list basic functions - Insert, View, Delete and Update.

### Requirements
* django
* boto3

## Steps to Start the Project
1. Clone the repository
2. Install the requirements needed
3. Create a TODO table in AWS DynamoDB with the attributes show  in in the ER Diagram - to_do_list.drawio.html
4. Set the below required environment variable.
    * DDB_TABLE_NAME: Dynamo DB table name for the ToDo
5. Configure aws in your environment by installing `awscli` and use the command - `aws configure` and provide the credentials.
6. Run the project using the command - `python3 manage.py runserver 0:8000`

`Note: Install the above requiremnts using command: pip3 install <module_name> in your command prompt or terminal`

