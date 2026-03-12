from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class feedback(BaseModel):

    sentiment: Literal["positive", "negative"] = Field(description='give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following text into positive or negative\n {feedback}\n{format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Write an appropriate response for this positive feedback\n{feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate response for this negative feedback\n{feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2|model|parser),
    (lambda x:x.sentiment=='negative', prompt3|model|parser),
    RunnableLambda(lambda x:"could not find sentiment")
)

chain = classifier_chain|branch_chain

result = chain.invoke({'feedback':'THIS phone is a Wonderful phone'})

print(result)

chain.get_graph().print_ascii()

