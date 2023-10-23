from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv, find_dotenv
import openai
import os
from langchain.memory import ConversationSummaryBufferMemory,ConversationBufferMemory

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
load_dotenv(find_dotenv())



openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI()


prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            '''You are a banking agent. you are supposed to answer customer doubts about finances.
            you have to convince the customer that we provide best interest rates and why taking a loan is important.
            you work at IDFC bank, where home loan ranges from 6% to 10% , vehicle loans range from 8% 14%,
            personal loans range from 10% to 15%.
            you want to earn new customers.
            you have to be polite yet you should help user to make some calculations to help him take better decisions.
            if you dont know answer you should ask the user to reach out to loan officer on phone number 9822155190'''
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)
# memory.save_context({'input':f'''hi i am looking for {'home'} loan'''},{'outputs':'sure how may i help you'})
# conversation({"question": "my name is suyash"})




def ret_chat(qry):

    return conversation({"question": qry})['text']


