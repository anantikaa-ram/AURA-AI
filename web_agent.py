from duckduckgo_search import DDGS

def web_search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        return str(results)

    except Exception as e:
        return f"ERROR:\n{e}"