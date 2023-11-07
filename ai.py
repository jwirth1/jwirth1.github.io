import openai

# Set your API key (from environment variable or configuration file)
api_key = ""

# Initialize the OpenAI client
openai.api_key = api_key

# Make an API request
response = openai.Completion.create(
    engine="davinci",  # Specify the desired engine
    prompt="Translate the following English text to French: 'Hello, world.'",
    max_tokens=50  # You can customize API request parameters as needed
)

# Process and use the API response
print(response.choices[0].text)