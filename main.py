from r2r import R2RClient
client = R2RClient()
hyde_response = client.rag(
    "What are the main themes in Shakespeare's plays?",
    vector_search_settings={
        "search_strategy": "hyde",
        "search_limit": 10
    }
)
print('hyde_response = ', hyde_response)