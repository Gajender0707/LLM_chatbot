from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["oLANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")



## setting up the model
model=ChatGroq(model="gemma2-9b-it")


## now try the model first

response=model.invoke([
    HumanMessage("hey i'm sanju"),
    AIMessage("remeber the details"),
    HumanMessage("what is the my name ")
])

print(response.content)