import openai
import asyncio
import nest_asyncio
nest_asyncio.apply()
from concurrent.futures import ThreadPoolExecutor

'''
This is a class that can be used to run GPT sentiment analysis in an async manner.
It uses the openai python library to run the GPT model.
Parameters:
    -valid OpenAI API key
    -data source (twitter, reddit, news)

Note: If you would like to run sentiment analysis on a data source other than the ones listed above, you can pass in the data source as a string.
'''

class AsyncGPT3:
    def __init__(self, apiKey, text_source):
        
        source_names = {'twitter': "Tweet's", 'reddit': "Reddit post's", 'news': "news headline's"}
        self.text_source = source_names.get(text_source.lower(), text_source.lower())
        openai.api_key = apiKey
        self.results = []
       
        
    def gpt_talk(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Decide whether a {0} sentiment is positive, neutral, or negative.\n\nHeadline:{1} \nSentiment:".format(self.textSource, text),
            temperature=0,
            max_tokens=7,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        return response['choices'][0].to_dict()['text'].lower().replace(' ', '')
    

    async def printThreaded(self, THREAD_POOL, text_list):   
        loop = asyncio.get_event_loop()
        coroutines = []
        for text in text_list:
            coroutine = loop.run_in_executor(THREAD_POOL, self.gpt_talk, text)
            coroutines.append(coroutine)
        results = await asyncio.gather(*coroutines)
        for res in results:
            self.results.append(res)
        return res
            
    def main(self, text_list):
        THREAD_POOL = ThreadPoolExecutor(100)
        with THREAD_POOL:
            loop = asyncio.get_event_loop()       
            loop.run_until_complete(self.printThreaded(THREAD_POOL, text_list))
        return self.results
            
            

