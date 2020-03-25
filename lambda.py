import json


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers':
            {
                'Content-Type': 'text/csv',
                'Content-Disposition': 'attachment; filename=testting.csv'
            },
        'csv': {
            'headers': 'year,month,day,company,model',
            'lines': [
                '1987,2,11,"Airbus","A320"',
                '1994,1,17,"Airbus","A330"',
                '2013,6,14,"Aiburs","A350"',
                '2005,4,27,"Airbus","A380"',
                '1997,11,16,"Boeing","777"',
                '1969,2,9,"Boeing","747"',
                '1967,4,9,"Boeing","737"'
            ]
        }
    }
