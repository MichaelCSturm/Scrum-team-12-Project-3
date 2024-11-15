
import pygame 
import sys 
import stock_visualization
from datetime import datetime

class variables:

    def q1(answer):
            answer = answer.upper()
            if len(answer) > 7 or len(answer) < 1 or answer.isalpha() == False:
                print("Hey make sure your answer is 1-7 alphabetical characters!")
                return 1
            variables.listOfInputs.append(answer)
            return 0
    def q2(answer):
            answer = answer.upper()
            if len(answer) != 1 or answer.isalpha() or int(answer)>2 or int(answer)<1:
                print("Hey make sure your answer is 1 or 2!")
                return 1
            if answer == "1":
                 variables.listOfInputs.append("LINE")
            if answer == "2":
                 variables.listOfInputs.append("BAR")
            return 0
    def q3(answer):
            answer = answer.upper()
            if len(answer) != 1 or answer.isalpha() or int(answer)>4 or int(answer)<1:
                print("Hey make sure your answer is 1 through 4!")
                return 1
            if answer =="1":
                 
                variables.listOfInputs.append("TIME_SERIES_DAILY")
            if answer =="2":
                variables.listOfInputs.append("TIME_SERIES_WEEKLY")
            if answer == "3":
                 variables.listOfInputs.append("TIME_SERIES_MONTHLY")
            if answer == "4":
                 variables.listOfInputs.append("TIME_SERIES_MONTHLY_ADJUSTED")
            return 0
    def q4(answer):
            answer = answer.upper()
            try:
                sendData =datetime.strptime(answer, '%Y-%m-%d')
                variables.stringStartDate = answer
                variables.listOfInputs.append(sendData)
                return 0
            except:
                print("Hey make sure your answer is formated like %Y-%m-%d'")
                return 1
    def q5(answer):
            answer = answer.upper()
            try:
                sendData =datetime.strptime(answer, '%Y-%m-%d')
                variables.stringEndDate= answer
                variables.listOfInputs.append(sendData)
                return 0
            except:
                print("Hey make sure your answer is formated like %Y-%m-%d'")
                return 1
    def sendData():
        stock_visualization.stockMaker(variables.listOfInputs[0],variables.listOfInputs[1],variables.listOfInputs[2],
                                       variables.listOfInputs[3],variables.listOfInputs[4], variables.stringStartDate,variables.stringEndDate)
    listofQuestions = ['Enter the stock symbol for the company you would like',
                   'Enter chart type you would like (line: 1/bar: 2)',
                   'Enter the time series function desired (TIME_SERIES_DAILY : 1, TIME_SERIES_WEEKLY : 2, TIME_SERIES_MONTHLY : 3, TIME_SERIES_MONTHLY_ADJUSTED: 4)',
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
    def runQuestions(question, asky):
        while(True):
            sentData = input(asky)
            returnedValue = question(sentData)
            print(variables.listOfInputs)
            if returnedValue == 1:
                 continue
            break
variables.runQuestions(variables.q1,variables.listofQuestions[0] )
variables.runQuestions(variables.q2,variables.listofQuestions[1] )
variables.runQuestions(variables.q3,variables.listofQuestions[2] )
variables.runQuestions(variables.q4,variables.listofQuestions[3] )
variables.runQuestions(variables.q5,variables.listofQuestions[4] )
variables.sendData()




    
    


    