from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv 

load_dotenv()

chat_model = ChatGroq(model="openai/gpt-oss-20b")

Prompt = ChatPromptTemplate.from_messages([

    ("system", "your are an {Profassion} expert on {topic}"),
    ("human", "hey  {Profassion} can explain it"),
    ("ai", "sure"),
    ('human', "{input}")

])

massage = Prompt.format_messages(
    Profassion = "teacher",
     topic = "AGENTIC AI",
     input = "langchain in 5 line"
    
)


result = chat_model.invoke(massage)

print(result.content)