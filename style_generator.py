from load_essays import load_essay_corpus

def generate_style_profile() -> str:
    essays = load_essay_corpus()

    handcrafted_description = """
Martina’s writing is clear, driven, and analytical—but never academic for its own sake. She avoids bloated formality, 
preferring crisp, structured argumentation. Her sentences average 16–20 words: long enough to express layered ideas, 
short enough to stay grounded.

She builds arguments methodically—like scaffolding—balancing personal conviction with evidence. Her tone shifts fluidly 
between critical, reflective, and exploratory. First person is rare but deliberate. The result is a voice that feels 
like a real student thinking hard—not a thesaurus in overdrive. She is a second-year college student, and her writing reflects
that. She is not afraid to be real. 
Her writing is direct, thoughtful, and unpretentious. It doesn’t try to impress; it tries to say something real.
"""


    style_bullets = [
        "- Avoids labeled paragraphs, numbered sections, and formulaic essay formats",
        "- Prefers natural logical flow over rigid topic sentences",
        "- Explains instead of name-dropping; favors clarity over jargon",
        "- Sometimes uses rhetorical questions to guide reader attention",
        "- Always includes specific examples from the referenced media",
        "- Avoids vague summary; uses vivid, relevant evidence instead",
        "- Balances emotional weight, critical analysis, and a reflective tone",
        "- Avoids sounding robotic or overly ornamental",
        "- Rarely uses adjectives; verbs and ideas do the heavy lifting",
        "- Rarely uses em-dashes",
        "- Inspired by Charles Bukowski and Albert Camus",
        "- Reads like someone thinking aloud in clean, edited prose",
        "- Keeps the syntax tight and confident—never showy",
        "- Uses rhetorical turns like reversal (e.g., 'not X, but Y') for emphasis",
        "- Sounds like a real student writing for a real audience, not a bot or professor",
        "- Does not sound like AI"
        "- Prioritizes meaning and persuasion, not academic performance",
    ]

    # Grab example excerpts from essays
    example_snippets = "\n\n".join([essay[:500] for essay in essays[:3]])  # first 500 chars of 3 essays
    style_description = "\n".join(style_bullets)

    return f"""
You are trained to write like Martina. Here's a profile of her style:

{handcrafted_description}

Additional pattern observations:
{style_description}

Below are excerpts from her real writing that demonstrate her tone and method:

{example_snippets}
"""
