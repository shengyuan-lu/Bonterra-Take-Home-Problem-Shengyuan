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

        print(f'Email report complete, file is {filename}')

    except APICallException as e:
        print(e.message)

    except:
        print('[Error]: An unknown error occurred. Program ended. ')
        print('[Action Required]: Please double check your API key and network, then run the program again. ')

if __name__ == '__main__':
    generate_report()