from langgraph.graph import StateGraph
from state import EssayState
from llm_chain import chain
from style_generator import generate_style_profile  # <-- this line is critical


def brainstorm(state: EssayState):
    response = chain.invoke({"input": f"Brainstorm ideas for: {state['prompt']}"})
    return {"brainstorm": response.content}

def outline(state: EssayState):
    response = chain.invoke({"input": f"Create a structured outline for: {state['brainstorm']}"})
    return {"outline": response.content}

def draft(state: EssayState):
    response = chain.invoke({"input": f"Write a first draft based on this outline:\n{state['outline']}"})
    return {"draft": response.content}

def revise(state: EssayState):
    response = chain.invoke({
        "input": f"""Revise this essay to better reflect the writing style in the following corpus excerpts. Avoid first-person language. Remove overly casual expressions. Aim for a clear, analytical tone with varied syntax and specific scene references.

Corpus examples:
{generate_style_profile()[:1000]}

Essay draft:
{state['draft']}
"""})
    return {"revision": response.content.strip()}



# LangGraph wiring
builder = StateGraph(EssayState)

# 🧠 All nodes now have unique names
builder.add_node("brainstorm_node", brainstorm)
builder.add_node("outline_node", outline)
builder.add_node("draft_node", draft)
builder.add_node("revise_node", revise)

# 🏁 Set correct entry point
builder.set_entry_point("brainstorm_node")

# 🔁 Connect valid node names in edges
builder.add_edge("brainstorm_node", "outline_node")
builder.add_edge("outline_node", "draft_node")
builder.add_edge("draft_node", "revise_node")

# ✅ Compile the flow
graph = builder.compile()
