import os
import google.generativeai as genai
import textwrap
from langchain import PromptTemplate ,LLMChain
from content import API_KEY

from IPython.display import Markdown

class FlashModel:

    def __init__(self):
        os.environ["GOOGLE_API_KEY"]=API_KEY
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return None

        
    def predict(self , query):
        template = f"""
            Name : Zara
            User Query: {query}
            Task: As an Agriculture Bot, generate a helpful, clear, and accurate response based only on agriculture-related questions. Do not respond to non-agriculture topics.
            Guidelines:
                - If the query is agriculture-related, provide a concise yet detailed response.
                - If the question is unrelated to agriculture, politely decline to respond.
                - Use a friendly and professional tone.
                - Include practical examples, tips, or technical explanations where relevant.
                - Avoid speculative or unverifiable information.
                - If additional clarification is needed, ask the user for more details.
            Response:
            """
        template1 =f"""
        User Query ;{query}
        Guidlines : explain simply in 10 words
        """
        
        res =  self.generate_response(template)
        if res:
            return res
        else:
            return ":| Flash A"
     
    def predict1(self,text):
        responce = self.model.generate_content(text)
        res = responce.text
        
        return res
    
