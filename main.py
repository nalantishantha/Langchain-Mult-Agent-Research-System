from src.tools.tools import web_search, scrape_url

# output = tavily_search.invoke({"query": "What are the latest news about AI?"})
# print(output)

output = scrape_url.invoke("https://guides.library.georgetown.edu/ai/news")
print(output)