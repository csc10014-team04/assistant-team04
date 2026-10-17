Function

def answer\_question(question: str) -> dict:

&#x20;   ...



Input

question: The user's question as a string (not empty)



Output

The function returns a dictionary:

{

&#x20;   "answer": "The answer to the question",

&#x20;   "success": True,

&#x20;   "error": None

}



Errors

INVALID\_INPUT: The question is empty.

SERVICE\_UNAVAILABLE: The AI service is unavailable.

TIMEOUT: The request takes too long.

INTERNAL\_ERROR: An unexpected error occurs.



Fallback

If the service fails, return a message saying the question cannot be answered right now.

