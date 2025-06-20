from graph import graph

if __name__ == "__main__":
    prompt = input("\n\nWhat’s your essay prompt?\n> ")
    result = graph.invoke({"prompt": prompt})
    print("\n\n=== Essay ===\n")
    print(result["revision"])
