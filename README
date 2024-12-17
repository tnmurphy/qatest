
# INSTRUCTIONS

## Information
Please read up about the `behave` testing framework for Python:

> https://behave.readthedocs.io/en/stable/index.html

This repository contains some code to test and a basic behave test environment which you should add to and modify.  The aim is to show that you can work with python and git and that you can understand Behavior Driven Development testing (BDD).

## Setting up python environment
These instructions reference a Linux environment. You will need python version 3.10 at least.  If you are using Windows the commands will be similar in most cases but not all.

1. Open a terminal and clone the repository

2. cd into the root of the repository

3. Create a virtual environment and activate it (Linux only):
```
python3 -m venv venv;
source venv/bin/activate
```

4. Install the required packages using the following command:
```
pip install behave
```

5. Run behave and confirm that the provided test works:  
```
behave
```

## Tasks

The overall task is to test a new API called "stats".  To make everything simpler the API endpoints are really just functions but they work a bit like HTTP endpoints. The stats module provides two functions:

*  median
*  mode

These are functions which take a list of numbers as a parameter and return an http-style Response object.
The response has a .json() method which will return a python dictionary containing the result
and a .status_code attribute which may return http codes like 200 (OK) or 422 (Unprocessable Entity).

If the status code is 200 then the response will contain a key "median" or a key "mode" which allows you to fetch the result e.g. 


```response.json()['median'] or response.json()['mode']```

If the status code is not 200 then the response will contain an "error" key with a message.

Example of how the API works:

```
from theapi.stats import median, mode

numbers = [ 1, 2, 3, 4, 5, 5, 6]

response = median(numbers)
if response.status_code == 200:
    print("Median = ", response.json()['median'])
else:
    print("Error finding median of ", numbers)

response = mode(numbers)
if response.status_code == 200:
    # the response is a list because there can be more than one number in a mode
    print("Mode = ", response.json()['mode'])
else:
    print("Error finding mode of ", numbers)
```

The output would look like this:

```
Median =  4
Mode =  [5]
```

### What to do?
*  This repository contains 1 behave scenario for testing the median API but you should add at least 1 more scenario.
*  There are no behave scenarios for the mode function - add some and see if you can find the main bug.

This means you will need to add at least 1 feature file (for the mode function) and 1 steps file (for mode also) and you will modify the feature and steps files for the median function that exist already.

#### Once you have finished 
You can zip your directory and email it back to us or you can make a pull request in github.

## More information about Median and Mode
### Median Definition
The median of a finite list of numbers is the "middle" number, when those numbers are listed in order from smallest to greatest.

If the data set has an odd number of observations, the middle one is selected (after arranging in ascending order). For example, the following list of seven numbers,

    1, 3, 3, 6, 7, 8, 9

has the median of 6, which is the fourth value.

If the data set has an even number of observations, there is no distinct middle value and the median is usually defined to be the arithmetic mean of the two middle values.[1][2] For example, this data set of 8 numbers

    1, 2, 3, 4, 5, 6, 8, 9

...has a median value of 4.5, that is ( 4 + 5 ) / 2 {\displaystyle (4+5)/2}. 

### Mode Definition
For a set of numbers, 'mode' refers to the most frequently occurring number. If there is more than one number with the same frequency then the mode is all of those numbers. If all the numbers have the same frequency then there is no mode.

Let's take the following data sets to calculate the mode.

    Example1: 2, 3, 5, 6, 5, 7, 5

In example 1, 5 has the highest frequency and hence the mode is [5].

    Example2: 5, 9, 1, 3, 7, 6, 6

In Example 2, 5,6 are both equally frequent so the mode is [5,6]

    Example3: 5, 9, 1, 3, 7, 6, 8

In Example 3, every value occurs once so there is no repetition. Therefore, the data set doesn't have a mode and the mode is []

