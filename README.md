# Fletcher
A Pytest-based automated test framework for API testing, designed for testing the Swagger PetStore public API.

## Purpose
Developed as a learning exercise, to gain experience building test frameworks.
Fletcher should function correctly, but it's not expected to be used by anyone else, or in a production environment.

## Structure
**clients:** Reusable code used to interact directly with the API.
**data:** Data that is used by the tests: For example, reusable payloads that are sent to the API.
**tests:** Test fixtures in conftest.py, and all the individual tests. 

## How To Use It
**Prerequisites**: Python version 3.14 or later, all python modules listed in requirements.txt.

**To run the tests:**
1. Using the terminal, navigate to the tests directory.
2. Run the tests using `pytest` (to run all tests), or `pytest` followed by the filename to run a single test.
