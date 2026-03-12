from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template= "Generate 5 important pointers from the text: {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':"Unemployment in India"})

print(result)

chain.get_graph().print_ascii()
