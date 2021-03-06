# -*- coding: utf-8 -*-
"""Tutorial on using the InfluxDB client."""

import argparse
from datetime import datetime
from influxdb import InfluxDBClient


def main(host='localhost', port=8086):
    """Instantiate a connection to the InfluxDB."""
    user = ''
    password = ''
    dbname = 'historisation'
    dbuser = ''
    dbuser_password = 'my_secret_password'
    query = 'select Float_value from analysis_data;'
    query_where = 'select Int_value from analysis_data where host=$host;'
    bind_params = {'host': 'server01'}
    json_body = [
        {
            "measurement": "analysis_data",
            "tags": {
                "type": "fire",
            },
            "time": str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')),
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Create database: " + dbname)
    client.create_database(dbname)

    # print("Create a retention policy")
    # client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    # print("Switch user: " + dbuser)
    # client.switch_user(dbuser, dbuser_password)

    print("Write points: {0}".format(json_body))
    client.write_points(json_body)

    # print("Querying data: " + query)
    # result = client.query(query)

    # print("Result: {0}".format(result))

    # print("Querying data: " + query_where)
    # result = client.query(query_where, bind_params=bind_params)

    # print("Result: {0}".format(result))

    # print("Switch user: " + user)
    # client.switch_user(user, password)

    # print("Drop database: " + dbname)
    # client.drop_database(dbname)


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)