# NGP-VAN-broadcastEmails-API-Practice
[API Reference](https://docs.ngpvan.com/reference/broadcastemails)

## A Brief Introduction To Program Files
- ```take_home_problem.py``` contains the main function of this take-home problem.
- ```api_manager.py``` contains a class that manages all aspects of API calls.
- ```api_call_exception.py``` contains a sub class of Exception that will be raised when APIManager encounters an error. The main function will catch this error and stop the program.


## Usage
This instruction assumes that you are using a linux-based system.

  1. Make sure Python 3 is installed on your machine. The version I used was ```3.11```. I also used the following Python libraries: ```requests```, ```csv```, ```os```, ```json```. There is a great chance that you already have them on your machine. If not, you need to install them prior to running this program.
  2. Clone this repo to your machine. You can do so by typing ```git clone git@github.com:shengyuan-lu/Bonterra-Take-Home-Problem-Shengyuan.git``` in your terminal.
  3. Change directory to ```Bonterra-Take-Home-Problem-Shengyuan```
  4. In the ```Bonterra-Take-Home-Problem-Shengyuan``` folder, create a ```.txt``` file called ```api_key.txt```. You can do so by typing ```touch api_key.txt``` in your terminal.
  5. On the first line of ```api_key.txt```, type your API key. Save the file. The program will automatically read your API key from this file. Alternatively, you can manually enter your API key when prompted.
  6. In the terminal, type ```python3 take_home_problem.py``` to run the program. The program will notify you when a report is generated. It may take a while for the program to run.
  7. You can view the email report by typing ```cat EmailReport.csv``` in the terminal

## Sample Output Based On The API Key Provided
![Screenshot 2023-02-26 at 01 52 31](https://user-images.githubusercontent.com/70995597/221403767-782ec7ba-8a65-4c98-8140-1f6fc92a28bc.jpg)

## Follow-up Questions
> Q: How long, roughly, did you spend working on this project? This won’t affect your evaluation; it helps us norm our problems to our expected time to complete them.

The project took me about 4 hours. I spent about 1 hour playing around with the API and understanding this project, 2 hours writing the program, 1 hour debugging and testing

> Q: Give the steps needed to deploy and run your code, written so that someone else can follow and execute them.

See ```Usage``` above.

> Q: What could you do to improve your code for this project if you had more time? Could you make it more efficient, easier to read, more maintainable? If it were your job to run this report monthly using your code, could it be made easier or more flexible? Give specifics where possible.

1. The current codebase contains several functions that share the same API call pattern. These functions differ only in the way they process callback data.  We can further simplify the code by creating a single function that handles the API calls. This function can accept parameters for endpoint, headers, and authentication, making it reusable for multiple functions. This improvement will result in more efficient and maintainable code, as well as reduce the risk of errors and inconsistencies. 

2. I would like to conduct more comprehensive testing of the program. At present, I only have access to one set of data. To ensure that the program is robust and reliable, I intend to test the program with multiple sets of data.

3. The current program interface is limited to the terminal, which may not be the most user-friendly option. I recognize that in a real-world scenario, this program would likely be used by campaign managers who require a more user-friendly interface. A web or mobile UI may be developed if I have more time.

4. Although it is highly unlikely, there may be situations where multiple variants perform equally well in terms of highest open rates. To account for this, I plan to implement a more robust solution that considers all of the highest-performing variants. Currently, I keep the first highest-performing variant from the API in cases of duplicates. 

5. If I were responsible for running this report on a monthly basis, I would automate the process by uploading the scripts to a remote server and configuring them to run automatically once a month. By doing so, I can reduce my workload and avoid the risk of errors or mistakes that may occur during manual execution.

> Q: Outline a testing plan for this report, imagining that you are handing it off to someone else to test. What did you do to test this as you developed it? What kinds of automated testing could be helpful here?

1. When I worked as a Software Quality Assurance Intern at Zoom, the test plans I created are scenario based. Here are a couple scenarios I come up with:

- When API key is not correct
  - Any error handling?

- When API key is correct

  - When API call returns 200:
    
    - When there are no email sent
    
    - When there are email sent, but without variants
    
    - When there are email sent with variants
    
      - When variants have the same performance (unlikely)
      - When variants have different performance

  - When API call does not return 200
    - Any error handling?

2. During the development of the program, I relied heavily on manual testing. This involved printing the output from my functions and manually comparing them to identify any inconsistencies or errors. While this approach helped me to identify obvious mistakes, it is not a sustainable solution in the long run.

3. To address this, I plan to implement automated testing by following the principles of test-driven development. This involves writing unit tests for each new feature or functionality as I develop them. By doing so, I can ensure that the code is thoroughly tested and any issues are identified and resolved early in the development process. It is essential to write unit tests that cover as much of the code as possible to ensure that the program meets the necessary requirements and specifications.
