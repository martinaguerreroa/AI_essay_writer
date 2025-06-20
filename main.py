from graph import graph

if __name__ == "__main__":
    prompt = input("What’s your essay prompt?\n> ")
    result = graph.invoke({"prompt": prompt})
    print("\n\n=== Final Essay Output ===\n")
    print(result["revision"])
