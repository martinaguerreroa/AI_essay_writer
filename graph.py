from langgraph.graph import StateGraph
from state import EssayState
from llm_chain import chain

def brainstorm(state: EssayState):
    return {"brainstorm": chain.run(input=f"Brainstorm ideas for: {state['prompt']}")}

def outline(state: EssayState):
    return {"outline": chain.run(input=f"Create a structured outline for: {state['brainstorm']}")}

def draft(state: EssayState):
    return {"draft": chain.run(input=f"Write a first draft based on this outline:\n{state['outline']}")}

def revise(state: EssayState):
    return {"revision": chain.run(input=f"Revise this draft into polished prose:\n{state['draft']}")}

builder = StateGraph(EssayState)
builder.set_entry_point("brainstorm")
builder.add_node("brainstorm", brainstorm)
builder.add_node("outline", outline)
builder.add_node("draft", draft)
builder.add_node("revise", revise)

builder.add_edge("brainstorm", "outline")
builder.add_edge("outline", "draft")
builder.add_edge("draft", "revise")

graph = builder.compile()
