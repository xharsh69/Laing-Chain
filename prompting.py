# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(model="openai/gpt-oss-20b" , temperature=0)

# prompt = ChatPromptTemplate.from_messages([

#     ("system", "you are best ai teacher"),
#     ("human","explain {topic} in simpel way.")
#     ])

# chain = prompt | model

# ruslt = chain.invoke({"topic": "who create you and how."})

# print(ruslt.content)



from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a programming teacher."),
    ("human", "Explain {topic} in simple English.")
])

messages = prompt.format_messages(
    topic="Python functions"
)

for message in messages:
    print(message)