import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def test_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"API Key found: {'Yes' if api_key else 'No'}")
    
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
        response = llm.invoke("Hello, are you working?")
        print("Response from Gemini 1.5 Flash:")
        print(response.content)
    except Exception as e:
        print(f"Error with gemini-1.5-flash: {e}")
        
    try:
        print("\nTrying gemini-1.5-flash-latest...")
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
        response = llm.invoke("Hello, are you working?")
        print("Response from Gemini 1.5 Flash Latest:")
        print(response.content)
    except Exception as e:
        print(f"Error with gemini-1.5-flash-latest: {e}")

if __name__ == "__main__":
    test_gemini()
