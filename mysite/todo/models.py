import os
import boto3
from boto3.dynamodb.conditions import Key

dynamo = boto3.resource('dynamodb')

class DynamoDB():
    
    # function to retrieve object of the table
    def table_object(self):
        """Get Table Object"""
        try:
            table = dynamo.Table(os.environ['DDB_TABLE_NAME'])
        except Exception as error:
            return error
        return table

    # function to insert into the table
    def insert(self, item):
        """Insert task in the table"""
        
        try:
            table = self.table_object()
            response = table.put_item(
                Item = item
            )
        except Exception as error:
            return error
            # print(response)
        return response
    
    # function to read from the table
    def read_single_item(self, entry_date, task_id):
        print(entry_date)
        print(task_id)
        """Read one specific item"""
        try:

            table = self.table_object()
            response = table.get_item(
                Key = {
                    'entry_date': entry_date,
                    'task_id': task_id
                }
            )
        except Exception as error:
            return error
            # print(response['Item'])
        return response
    
    # function to read all items from the table
    def read_all(self):
        """Read all items"""
        try:

            table = self.table_object()
            response = table.scan()
            # print(response['item'])
        except Exception as error:
            return error
        return response
    
    # function to update item
    def update(self, entry_date, task_id):
        """Update items"""
        try:

            table = self.table_object()
            response = table.update_item(
                Key = {
                    'entry_date': entry_date,
                    'task_id': task_id
                },
                ExpressionAttributeNames = {
                    "#status": "status"
                },
                ExpressionAttributeValues = {
                    ":s": "complete"
                },
                UpdateExpression = "set #status = :s",
            )
            # print(response)
        except Exception as error:
            return error
        return response
    
    # function to delete item
    def delete_single_item(self, entry_date, task_id):
        """Delete Item"""
        try:
            table = self.table_object()
            response = table.delete_item(
                Key = {
                    'entry_date' : entry_date,
                    'task_id' : task_id
                }
            )
        except Exception as error:
            return error
        # print(response['Items'])
        return response
    
    # function to query over the table
    def query(self, entry_date):
        """Query"""
        try:

            table = self.table_object()
            response = table.query(
                KeyConditionExpression=Key('entry_date').eq(entry_date)
            )
        except Exception as error:
            return error
        return response

