# langchain-openai-db-query-agent
A langchain openai based application concept to query local sqlite database.

## Tools and language:
- python
- langchain
- openai
- pyboxen (verbose output beautifier)
- pipenv (for isolated python virtual environment)

## Setup to run in local (_this has been tested on mac_)
- install python 
- install pipenv
  `pip install pipenv`
- run the below command to install all dependencies from the pipfile
  `pipenv install`
- create an isolated virtual environemt for the app to run in
  `pipenv shell`
- now run your application
  `python main.py`

## Sample detailed output (Query: How many user are there in the databse?)

<img width="1122" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/ca846001-4c89-45d2-b08e-08fe93bc4255">
<img width="1127" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/39a27efa-b394-435e-8fd6-dfb2c99c8acc">
<img width="1122" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/65b40633-78f6-4566-8462-5d08872eac29">
<img width="1115" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/29472ba7-f951-43ed-94cf-8320d68bf3ba">

## Architecture and Flowchart

  To get an understanding of how it works on different case scenarios, below are some basic snapshots.
  For more detailed, please visit the [miro link](https://miro.com/app/board/uXjVKKYwQFc=/)
  
### Process execution flowchart (courtesy: Udemy tutorials)

<img width="1069" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/3fccd697-572e-49c8-8696-bae9b904c3a8">

### Concept of ChatGPT functions using code (Tool from Langchain)

<img width="920" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/f6cb41ea-2ac7-4310-8a6c-49016d03edb4">

### SQLite db details

<img width="756" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/4f674d92-4d34-4db6-b652-bd4ea8e76b90">


### Database query error handling to make chatgpt to assume alternate solution or convey something went wrong

<img width="1035" alt="image" src="https://github.com/rohan1443/langchain-openai-db-query-agent/assets/12879983/81217836-3e51-4281-85dd-552b07e73b8e">

