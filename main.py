# Import configuration modules
from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

# Initialize configuration
config = Configuration()

# Customize your config here
# (See the Configuration Details section below for more options)
config.set_provider_config("llm", "DeepSeek", {"model": "deepseek-reasoner"})
config.set_provider_config("embedding", "GeminiEmbedding", {"model": "text-embedding-004"})
init_config(config=config)

# Load data from local files
# from deepsearcher.offline_loading import load_from_local_files
# load_from_local_files(paths_or_directory="data")

# (Optional) Load data from websites
# Requires FIRECRAWL_API_KEY environment variable
from deepsearcher.offline_loading import load_from_website
load_from_website(urls=["https://www.wikipedia.org/"])

# Query your data
result = query("Write a report about apple market research.")  # Replace with your question
print(result)