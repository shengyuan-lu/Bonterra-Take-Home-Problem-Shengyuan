import csv
from api_manager import APIManager
from api_call_exception import APICallException

def generate_report(filename='EmailReport.csv'):
    """
    
    :param filename: a file name for the generated .csv file, default is provided
    :return: No return, the .csv file is written to the disk
    """

    try:
        manager = APIManager()

        result = manager.get_result()

        fields = ['Email Message ID', 'Email Name', 'Recipients', 'Opens', 'Clicks', 'Unsubscribes', 'Bounces', 'Top Variant']

        # write to csvfile
        with open(filename, 'w') as csvfile:

            # create a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # write fields
            writer.writeheader()

            # write email rows
            for email in result:
                writer.writerow(email)

    except APICallException as e:
        print(e.message)

if __name__ == '__main__':
    generate_report()