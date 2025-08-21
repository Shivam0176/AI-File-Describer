from google import genai
from google.genai import types
import mimetypes

GEMINI_API_KEY = "AIzaSyDwfBwNVK1zQ2zSYZg1u01aNMmIKEtLEIU"

client = genai.Client(api_key=GEMINI_API_KEY)


def describe_File(file_path):
    mime_type,_ = mimetypes.guess_type(file_path.name)
    print(mime_type)


    # f = open(file_path,"rb")
    image_bytes = file_path.read()

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type),
                'describe this file'

        ]
    )

    return response.text


