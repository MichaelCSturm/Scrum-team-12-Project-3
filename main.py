
import pygame 
import sys 
import stock_visualization
from datetime import datetime

class variables:
    listofQuestions = ['Enter the stock symbol for the company you would like',
                   'Enter chart type you would like (line: 1/bar: 2)',
                   'Enter the time series function desired (TIME_SERIES_DAILY, TIME_SERIES_WEEKLY, etc.)',
                   'Enter the beginning date in YYYY-MM-DD ',
                   'Enter the end date in YYYY-MM-DD format', 
                   'Processin'
                   ]
    question_text = listofQuestions[0]
    questionIndex = 0
    listOfInputs = []
    secretQuestion = "Enter an end date not below the begining date."
    errorText = ''
    stringStartDate = ''
    stringEndDate =''


# pygame.init() will initialize all 
# imported module 
while True:
    print(variables.listofQuestions[0])
    answer = input()
    answer = answer.upper()
    if len(answer) > 7 or len(answer) < 1 or answer.isalpha() == False:
        print("Hey make sure your answer is 1-7 alphabetical characters!")
        continue
    variables.listOfInputs.append(answer)
    break
while True:
    print(variables.listofQuestions[1])
    answer = input()
    answer = answer.upper()
    if len(answer) != 1 or answer.isalpha() or int(answer)>2 or int(answer)<1:
        print("Hey make sure your answer is 1 or 2!")
        continue
    variables.listOfInputs.append(answer)
    break
while True:
    print(variables.listofQuestions[2])
    answer = input()
    answer = answer.upper()
    if len(answer) != 1 or answer.isalpha() or int(answer)>4 or int(answer)<1:
        print("Hey make sure your answer is 1 through 4!")
        continue
    variables.listOfInputs.append(answer)
    break
