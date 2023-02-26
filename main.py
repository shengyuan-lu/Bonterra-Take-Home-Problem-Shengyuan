from api_manager import APIManager

def main():
    manager = APIManager()

    print(manager.get_result())

if __name__ == '__main__':
    main()