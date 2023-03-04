# AsyncGPT3 Sentiment Analysis
This is a Python class that can be used to run GPT-3 sentiment analysis in an asynchronous manner. It uses the OpenAI Python library to run the GPT-3 model.

## Installation
Install the OpenAI package by running ```!pip install openai``` in your Python environment.
Add nest_asyncio and concurrent.futures libraries by running ```!pip install nest_asyncio```

## Usage
To use this class, you need a valid OpenAI API key and specify the data source for sentiment analysis. Currently, the class supports three data sources, Twitter, Reddit, and News. However, if you want to analyze sentiment for other data sources, you can pass them as a string.

Here is an example usage:

```python
import AsyncGPT3

api_key = "YOUR_OPENAI_API_KEY"
data_source = "twitter"

asyncGPT = AsyncGPT3(api_key, data_source)
results = asyncGPT.main(["Text to analyze 1", "Text to analyze 2"])

print(results)
```
The main function takes a list of text inputs that need sentiment analysis. The function will return a list of sentiments (positive, neutral, or negative) for each input text.
