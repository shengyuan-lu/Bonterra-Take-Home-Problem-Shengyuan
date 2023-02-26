# Bonterra-Take-Home-Problem

## A Brief Introduction To Program Files
- ```take_home_problem.py``` contains the main function of this take-home problem.
- ```api_manager.py``` contains a class that manages all aspects of API calls.
- ```api_call_exception.py``` contains a sub class of Exception that will be raised when APIManager encounters an error. The main function will catch this error and stop the program.


## Usage
This instruction assumes that you are using a linux-based system.

  1. Make sure Python 3 is installed on your machine. The version I used was ```3.11```. I am also using the following Python libraries: ```requests```, ```csv```, ```os```, ```json```. There is a great chance that you already have them on your machine. If not, you need to install them prior to running this program.
  2. Clone this repo to your machine. You can do so by typing ```git clone git@github.com:shengyuan-lu/Bonterra-Take-Home-Problem-Shengyuan.git``` in your terminal.
  3. In the ```Bonterra-Take-Home-Problem-Shengyuan``` folder, create a ```.txt``` file called ```api_key.txt```. You can do so by typing ```touch api_key.txt``` in your terminal.
  4. On the first line of ```api_key.txt```, type your API key. The program will automatically read your API key from this file. Alternatively, you can manually enter your API key when prompted.
  5. Open terminal, and change directory to ```Bonterra-Take-Home-Problem-Shengyuan```
  6. In the terminal, type ```python3 take_home_problem.py``` to run the program
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

2. I would like to conduct more comprehensive testing of the program. At present, I only have access to one set of data. To ensure that the program is robust and reliable, I intend to follow the principles of test-driven development. This means that I will write automated tests for each new feature as I develop them. By doing so, I can ensure that the program is thoroughly tested and any issues are identified and resolved early in the development process. 

3. The current program interface is limited to the terminal, which may not be the most user-friendly option. I recognize that in a real-world scenario, this program would likely be used by campaign managers who require a more user-friendly interface. A web or mobile UI may be developed if I have more time.

> Q: Outline a testing plan for this report, imagining that you are handing it off to someone else to test. What did you do to test this as you developed it? What kinds of automated testing could be helpful here?
