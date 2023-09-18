# IDS_706 - Data Engineering Systems 
## Mini-Project 3 : Polars Descriptive Statistics Script

[![CI](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/actions/workflows/cicd.yml)

***

### Goal of the Project
Mini-Project 3 modifies [this existing Github template](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems) by handling the loading and manipulation of a movies dataset stored in a `.csv` file using the Polars library. 

This entails extracting meaningful insights from the dataset by generating descriptive statistics. This project also represents the relationship between popularity ratings and average ratings out of 10 as a scatter plot. This project also identifies and presents the movies with the highest ratings from the dataset. 

The accompanying Makefile automates essential development tasks, making it easier for developers to maintain code quality, run tests, and streamline the development workflow.

Note: Summary Report on the dataset is generated as a `.html` file.  

Dataset used: [Top-Rated Movies Data Set](https://www.kaggle.com/datasets/khalidalam980/top-rated-movies-data-set)

***

### Commands to Run the Repo

To run the project, you can use the Makefile and follow these commands:
1. ```
   # To install the required the python packages
   make install
   ```
2. ```
   # To check code style
   make lint
   ```
3. ```
   # To run tests
   make test
   ```
4. ```
   # To format the code
   make format
   ```
5. ```
   # To perform all the above tasks (install, test, format, lint)
   make all
   ```

***

### Result

1. On running ```make lint```:

![make lint](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_3/assets/143756865/7c54982b-f637-4027-9cae-04152e4b3807)

2. On running ```make test```, it passes the test:

![make test](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_3/assets/143756865/3a7218fc-169b-4e71-82a6-86a951f45a76)

3. On running ```make format```:

![make format](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_3/assets/143756865/6f1410c9-048e-462c-aac4-e04cedfdcf7a)

***

### Output from test_main.py

On running test_main.py, it displays the descriptive statistics from the dataset as well as the top rated movies. This file generates and displays the plot for popularity vs vote_average. It also ensures that there is a valid value returned from display_highest_votes() (from main.py) using the assert statement.

![ss1](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_3/assets/143756865/df076ba9-d15a-4e08-8090-814dc26356c5)
![ss2](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_3/assets/143756865/49d78566-31bc-4f1e-bc83-fc00b404528d)

***

### Data Visualization (popularity vs vote_average scatter plot)

![graph polars](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_3/assets/143756865/63d5d632-4062-413f-bd33-9b57174d1eb2)

***
