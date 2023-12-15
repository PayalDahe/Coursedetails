print('COURSE DETAILS')
print('PYTHON PROGRAMING FOR DATA SCIENCE')
print('1.Introdiction')
print('2.Basic of Python')
print('3.Error and Exception Handling')
print('4.Functions')
print('5.OOPS')
print('6.INTRODUCTION TO DATA SCIENCE')
print('7.STATISTICS')
print('8.EXPLORATORY DATA ANALYSIS AND DATA VISUALIZATION')
x=int(input('Enter Your Choice'))
if x==1:
    def Introduction():
        print('***Introduction***')
        print('What is Python')
        print('History')
        print('Why Python Prefer For Data Science')
        print('Insatallation of Pyhton/Jupyter/Notebook/SPYDER')
    Introduction()
elif x==2:
    def Basic_of_Python():
        print('***Basic of Python***')
        print('Keywords')
        print('Built-in Function')
        print('Data Types')
        print('Importing & Exporting Data From Python into Various Format')
    Basic_of_Python()
elif x==3:
    def Error_and_Exception_Handling():
        print('***Error and Exception Handling***')
        print('Error in Python')
        print('Abnormal Terminations')
        print('Exception Handling Method')
        print('Ignoring Errors')
        print('Assertions and Effective Usage of Assertions')
    Error_and_Exception_Handling()
elif x==4:
    def Functions():
        print('***Functions***')
        print('User Define Functions')
        print('Parameters')
        print('Nested Functions')
        print('Sorting Collections')
    Functions()
elif x==5:
    def OOPS():
        print('***OOPS***')
        print('Method And Inheritance')
        print('Abstractions and Encapsulations')
        print('Classes')
        print('Walking Directory Trees')
        print('initialise')
    OOPS()
elif x==6:
    def INTRODUCTION_TO_DATA_SCIENCE():
        print('***INTRODUCTION TO DATA SCIENCE***')
        print('What is Data Science')
        print('What is Big Data')
        print('What is Machine Learning')
        print('what is Analytic')
        print('What Data Analysis And Data Mining')
    INTRODUCTION_TO_DATA_SCIENCE()
elif x==7:
    def STATISTICS():
        print('***STATISTICS***')
        print('Definition and Computation of Probability ')
        print('Sampling and Sampling Distribution')
        print('Contigency Table')
    STATISTICS()
elif x==8:
    def EXPLORATORY_DATA_ANALYSIS_AND_DATA_VISUALIZATION():
        print('***EXPLORATORY DATA ANALYSIS AND DATA VISUALIZATION***')
        print('What is EDA and Why is Required')
        print('Outlier Treatment')
        print('Graphs')
        print('Bar Chart')
        print('Variable Selection')
    EXPLORATORY_DATA_ANALYSIS_AND_DATA_VISUALIZATION()