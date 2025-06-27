#export GEMINI_API_KEY=your_key_here

from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyCwmX8wbkyY0vMYWYr7FGOeNlfKxNsQxSA")

cfg = None

cond = 1
while cond != 4:
    try:
        cond = int(input("Select a Mode\n(1) Prompt Model, (2) Model Settings, (3) Reset Settings, (4) Exit: "))
        if cond == 4:
            continue
    except TypeError:
        print("Not a valid input! Please input a number.")
        continue
    except ValueError:
        print("Not a valid input! Please input a number.")
        continue
    else:
        if cond == 3:
            cfg = None
            continue
        if cond == 2:
            try:
                max_tokens = int(input("Input Max Output Tokens (Integer): "))
                temperature = float(input("Temperature: "))
                top_p = float(input("Top P: "))
                top_k = int(input("Top K (Integer): "))
                cfg = types.GenerateContentConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                )
            except:
                print("Invalid values! Try again.")
        else:
            prompt = input("Input prompt (MAX 600 CHARACTERS): ")
            if len(prompt) > 600:
                print("Please keep prompt under 600 characters!")
                continue
            if cfg == None:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=prompt,
                )
            else:
                response = client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=prompt,
                    config=cfg,
                )
            if response.text:
                print(response.text)
            elif response.candidates:
                try:
                    print(response.candidates[0].content.parts[0].text)
                except Exception as e:
                    print("No valid content returned.")
            else:
                print("Response returned no candidates.")
