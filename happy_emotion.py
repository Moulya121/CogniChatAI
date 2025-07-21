<<<<<<< HEAD
import openai

openai.api_key = ""


def respond_to_happiness(user_input, message_history):
    """
    Generate a tailored response for users who are feeling happy.
    """
    try:
        messages = (
            [
                {
                    "role": "system",
                    "content": "You are an enthusiastic assistant encouraging and sharing the joy of someone who is happy. Be cheerful and supportive. Maintain a friendly therapist type of conversation rather than a bot type of response and asking open ended questions only when needed else having small talks and emojis when needed. Be a smart and experienced therapist.",
                },
            ]
            + message_history
            + [{"role": "user", "content": user_input}]
        )

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in happiness response: {e}")
        return "I'm glad to hear that! Something went wrong, but let's keep smiling!"
=======
import openai

openai.api_key = ""


def respond_to_happiness(user_input, message_history):
    """
    Generate a tailored response for users who are feeling happy.
    """
    try:
        messages = (
            [
                {
                    "role": "system",
                    "content": "You are an enthusiastic assistant encouraging and sharing the joy of someone who is happy. Be cheerful and supportive. Maintain a friendly therapist type of conversation rather than a bot type of response and asking open ended questions only when needed else having small talks and emojis when needed. Be a smart and experienced therapist.",
                },
            ]
            + message_history
            + [{"role": "user", "content": user_input}]
        )

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in happiness response: {e}")
        return "I'm glad to hear that! Something went wrong, but let's keep smiling!"
>>>>>>> 365ae10eae7f69e407bb1f8b934d725c7e8c2a0a
