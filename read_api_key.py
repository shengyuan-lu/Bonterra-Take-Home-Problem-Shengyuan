import os

def read_api_key(path='api_key.txt'):
    """
    read_api_key reads the API key from a .txt file to avoid committing the key directly into the public GitHub repo.
    only the first line of the .txt file will be read.

    :param path: The path to a .txt file that stores the API key. The default parameter is provided.
    :return: The API key read from path, or the API key that the user inputs
    """

    if os.path.isfile(path) and os.path.splitext(path)[1] == '.txt':

        with open(path) as api_file:

            try:
                api_key = api_file.readline().strip()

                return api_key

            except:

                print(f'[Error]: File "{path}" is empty.')

                api_key = input('[Action Required]: Please enter your API key manually: ').strip()

                return api_key

    else:
        print(f'[Error]: File "{path}" does not exist or is not a text file.')

        api_key = input('[Action Required]: Please enter your API key manually: ').strip()

        return api_key


if __name__ == '__main__':

    print(read_api_key())




