from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sentiment classifier. Follow the examples."),

    ("human", "Text: This product is amazing!"),
    ("ai", "Sentiment: Positive"),

    ("human", "Text: The service was terrible."),
    ("ai", "Sentiment: Negative"),

    ("human", "Text: {input}")
])

input1 = prompt.invoke({
    "input": "The product works bad."
})


response = model .invoke(input1)

print(response.content)

