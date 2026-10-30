from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in Python."),
    ("human", "Explain {concept} for a {level} student.")
])

result = prompt.invoke({
    "concept": "pointers",
    "level": "intermediate"
})

print(result.to_messages())