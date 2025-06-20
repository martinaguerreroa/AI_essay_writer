from typing import TypedDict, Optional

class EssayState(TypedDict):
    prompt: str
    brainstorm: Optional[str]
    outline: Optional[str]
    draft: Optional[str]
    revision: Optional[str]
