from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from style_guide import style_sample

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", f"You are an academic essay-writing assistant trained in the following style:\n\n{style_sample}"),
    ("human", "{input}")
])

chain = LLMChain(llm=llm, prompt=prompt)
