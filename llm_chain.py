import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from style_guide import style_sample

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", f"You are an academic essay-writing assistant trained in the following style:\n\n{style_sample}"),
    ("human", "{input}")
])

# Use new-style chaining
chain = prompt | llm

from style_generator import generate_style_profile

style_sample = generate_style_profile()  # ← now pulled from real essays
