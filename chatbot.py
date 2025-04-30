from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
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

# response=model.invoke([
#     HumanMessage("hey i'm sanju"),
#     AIMessage("remeber the details"),
#     HumanMessage("what is the my name ")
# ])

# print(response.content)
store={}
def get_chat_history(session_id:str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]



runnable=RunnableWithMessageHistory(model,get_chat_history)
config={"configurable":{"session_id":"user_1"}}

# response = runnable.invoke(
#     {"input": "Hello"},
#     config={"configurable": {"session_id": "user123"}}
# )



# m2=runnable.invoke(
#     [HumanMessage("Hey my name is sanju and mca student ")],
#     config
# )
# print(m2.content)

# m3=runnable.invoke(
#     [HumanMessage(content="Hey what is my name and field of study?? ")],
#     config
# )

# print(m3.content)


m4=runnable.invoke(
    [HumanMessage(content="Hey who i'm   ")],
    {"configurable":{"session_id":"user_1"}}
)

print(m4.content)