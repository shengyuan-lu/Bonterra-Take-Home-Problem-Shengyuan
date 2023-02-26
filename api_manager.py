import requests
import os
import json
from api_call_exception import APICallException

class APIManager:

    def __init__(self, endpoint='https://api.myngp.com/v2/broadcastEmails', api_key_path='api_key.txt'):
        self.api_key = self.read_api_key(api_key_path)
        self.general_endpoint = endpoint

    def read_api_key(self, path):
        """
        avoid to hardcode API key in a GitHub repo by reading the API key from a .txt file

        :param path: the path of a .txt file that stores the API key
        :return: the API key
        """

        # verify if the path is valid and the path points to a .txt file
        if os.path.isfile(path) and os.path.splitext(path)[1] == '.txt':

            # open file, read content
            with open(path) as file:

                try:
                    api_key = file.readline().strip()

                    return api_key

                # ask for manual input when file is empty
                except:

                    print(f'[Error]: File [{path}] is empty.')

                    api_key = input('[Action Required]: Please enter your API key manually: ').strip()

                    return api_key

        else:
            # ask for manual input when file does not exist or is not a .txt file
            print(f'[Error]: File [{path}] does not exist or is not a text file.')

            api_key = input('[Action Required]: Please enter your API key manually: ').strip()

            return api_key


    def get_sent_emails_id(self):
        """

        :return: a list of sent email ids

        sample id_list returned:
        [469, 470, 468, 467, 466, 464, 465, 463, 462]

        """

        # Define Basic Authentication credentials using API key
        auth = requests.auth.HTTPBasicAuth('apiuser', self.api_key)

        # Define request headers (as shown in the /broadcastEmails API doc)
        headers = {
            'accept': 'application/json'
        }

        # Make API request using requests library
        response = requests.get(self.general_endpoint, headers=headers, auth=auth)

        # Check for successful response
        if response.status_code == 200:

            # Extract data from response
            data = json.loads(response.text)

            emails = data['items']

            id_list = list()

            for email in emails:
                id_list.append(email['emailMessageId'])

            return id_list

        elif response.status_code == 400:
            # Raise exception
            raise APICallException(f'[Error]: response of {self.general_endpoint} has 400 Bad Request. Program Ended.')


    def get_sent_email_details_by_id(self, email_id):
        """

        :param email_id: identifies the email to be retrieved
        :return: the detail of the email based on the email_id

        sample email detail returned:

        {
            'emailMessageId': 469,
            'name': 'Fragile Webs',
            'variants': [{
                'emailMessageId': 0,
                'emailMessageVariantId': 490,
                'name': 'Fragile Webs',
                'subject': 'Fragile Webs'
            }, {
                'emailMessageId': 0,
                'emailMessageVariantId': 491,
                'name': 'Life in the Balance',
                'subject': 'Life in the Balance'
            }, {
                'emailMessageId': 0,
                'emailMessageVariantId': 492,
                'name': 'Fragile Webs_Winner',
                'subject': 'Fragile Webs'
            }],
            'statistics': {
                'recipients': 450,
                'opens': 14,
                'clicks': 2,
                'unsubscribes': 1,
                'bounces': 6
            }
        }
        """

        # Get the new end point based on the email_id
        specific_end_point = os.path.join(self.general_endpoint, str(email_id))
        specific_end_point.rstrip('/')
        specific_end_point += '?$expand=statistics'

        # Define Basic Authentication credentials using API key
        auth = requests.auth.HTTPBasicAuth('apiuser', self.api_key)

        # Define request headers (as shown in the /broadcastEmails/{emailMessageId} API doc)
        headers = {
            'accept': 'application/json'
        }

        # Make API request using requests library
        response = requests.get(specific_end_point, headers=headers, auth=auth)

        # Check for successful response
        if response.status_code == 200:

            # Extract data from response
            email_details = json.loads(response.text)

            return email_details

        elif response.status_code == 400:
            # Raise exception
            raise APICallException(f'[Error]: response of {specific_end_point} has 400 Bad Request. Program Ended.')

        elif response.status_code == 404:
            # Raise exception
            raise APICallException(f'[Error]: response of {specific_end_point} has 404 Page Not Found. Program Ended.')


    def get_highest_performed_variant_from_details(self, email_details):
        """

        :param email_details: the detail of the email to retrieve top variant name from
        :return: the highest performed variant name

        sample variant name returned:
        'Fragile Webs_Winner'
        """

        variants = email_details['variants']

        if len(variants) == 0:
            return ''

        else:
            email_id = email_details['emailMessageId']

            max_rate = float('-inf')
            max_name = ''

            for variant in variants:

                # Get the new end point based on the email_id
                specific_end_point = os.path.join(self.general_endpoint, str(email_id), 'variants', str(variant['emailMessageVariantId']))
                specific_end_point.rstrip('/')
                specific_end_point += '?$expand=statistics'

                # Define Basic Authentication credentials using API key
                auth = requests.auth.HTTPBasicAuth('apiuser', self.api_key)

                # Define request headers (as shown in the /broadcastEmails/{emailMessageId}/variants/{emailMessageVariantId} API doc)
                headers = {
                    'accept': 'application/json'
                }

                # Make API request using requests library
                response = requests.get(specific_end_point, headers=headers, auth=auth)

                # Check for successful response
                if response.status_code == 200:

                    # Extract data from response
                    variant_details = json.loads(response.text)

                    # Calculate rate based on opens
                    rate = variant_details['statistics']['opens'] / variant_details['statistics']['recipients']

                    if rate > max_rate:
                        max_rate = rate
                        max_name = variant_details['name']

                elif response.status_code == 400:
                    # Raise exception
                    raise APICallException(f'[Error]: response of {specific_end_point} has 400 Bad Request. Program Ended.')

                elif response.status_code == 404:
                    # Raise exception
                    raise APICallException(f'[Error]: response of {specific_end_point} has 404 Page Not Found. Program Ended.')

            return max_name


    def convert_to_csv_ready_format(self, detail):
        """
        :param detail: an email detail dict
        :return: parsed dict for .csv generation
        """

        result = dict()

        result['Email Message ID'] = detail['emailMessageId']
        result['Email Name'] = detail['name']
        result['Recipients'] = detail['statistics']['recipients']
        result['Opens'] = detail['statistics']['opens']
        result['Clicks'] = detail['statistics']['clicks']
        result['Unsubscribes'] = detail['statistics']['unsubscribes']
        result['Bounces'] = detail['statistics']['bounces']
        result['Top Variant'] = detail['top_variant']

        return result


    def get_result(self):

        try:

            emails = list()

            for id in self.get_sent_emails_id():

                detail = self.get_sent_email_details_by_id(id)

                detail['top_variant'] = self.get_highest_performed_variant_from_details(detail)

                emails.append(self.convert_to_csv_ready_format(detail))

            return sorted(emails, key=lambda x: x['Email Message ID'], reverse=True)

        except APICallException as e:

            print(e.message)

            return list()
