from litellm import completion
from config import PROVIDER_MODEL as MODEL
stream = completion(model=MODEL, messages=[{"role":"user","content":"Write 3 sentences about a traveling cat."}], stream=True)
for chunk in stream:
    delta = chunk.choices[0].delta.get("content") if chunk.choices and chunk.choices[0].delta else None
    if delta: print(delta, end="", flush=True)
print()