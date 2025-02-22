from openai import OpenAI

from api.common.config import (OPENAI_API_KEY)

import openai
BASE_URL = "https://models.inference.ai.azure.com"  # Azure OpenAI endpoint
MODEL_NAME = "gpt-4o"  # Model to be used

# Configure the OpenAI client for Azure
client = openai.OpenAI(api_key=OPENAI_API_KEY, base_url=BASE_URL)

def ask_to_openai(prompt, system_content):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
