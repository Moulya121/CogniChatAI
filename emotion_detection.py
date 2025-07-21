# import openai

# # Configure OpenAI API key
# openai.api_key = ""


# def detect_emotion(user_input, message_history):
#     """
#     Detects the user's current emotion based on the message history and latest input.
#     """
#     try:
#         # Only include user messages in the emotion analysis
#         user_history = [msg for msg in message_history if msg["role"] == "user"]

#         messages = (
#             [
#                 {
#                     "role": "system",
#                     "content": (
#                         "You are an assistant that detects emotions in text. "
#                         "Analyze the user's current state and return one of these emotions only these emotions thats it. nothing else all small and one word. if still confused about emotion then map into one of the closest emotion below: I repeat it should strictly reply only one of the emotions: "
#                         "frustrated, depressed, angry, sad, excited, happy, bored, lonely, or anxious."
#                     ),
#                 },
#             ]
#             + user_history
#             + [{"role": "user", "content": user_input}]
#         )

#         # Call OpenAI API
#         response = openai.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=messages,
#             temperature=0.5,
#             max_tokens=10,  # Limit response to a single emotion keyword
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#         )

#         # Extract and validate emotion
#         emotion = response.choices[0].message.content.strip().lower()
#         valid_emotions = [
#             "frustrated",
#             "depressed",
#             "angry",
#             "sad",
#             "excited",
#             "happy",
#             "bored",
#             "lonely",
#             "anxious",
#         ]
#         return emotion if emotion in valid_emotions else emotion # "neutral"
#     except Exception as e:
#         print(f"Error in emotion detection: {e}")
#         return "neutral"









from transformers import pipeline

# Load BERT emotion classifier model
emotion_classifier = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")

# Map BERT emotion labels to your system's labels
emotion_map = {
    "sadness": "sad",
    "joy": "happy",
    "anger": "angry",
    "fear": "anxious",
    "love": "excited",
    "surprise": "excited",
    "disgust": "frustrated",
    "neutral": "bored"
}

def detect_emotion(user_input, message_history=None):
    """
    Detects emotion using BERT instead of GPT.
    Only the latest user input is used.
    """
    try:
        result = emotion_classifier(user_input)[0]  # Top prediction
        label = result['label'].lower()  # e.g., "sadness"
        return emotion_map.get(label, "neutral")  # Return mapped label
    except Exception as e:
        print(f"Error in emotion detection (BERT): {e}")
        return "neutral"
