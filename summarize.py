from litellm import completion
from config import PROVIDER_MODEL as MODEL

def summarize(text, length="brief"):
    lengths = {"brief":"in 1–2 sentences","medium":"in 3–4 sentences","detailed":"in 5–6 sentences with key points"}
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"You are an expert summarizer. Summarize {lengths.get(length,'in 2–3 sentences')}"},
            {"role":"user","content":text}
        ],
        temperature=0.3, max_tokens=180,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    sample = """Recent advances in AI… (Supported models
All models in the Gemini family support text generation. To learn more about the models and their capabilities, visit the Models page.

Best practices
Prompting tips
For basic text generation, a zero-shot prompt often suffices without needing examples, system instructions or specific formatting.

For more tailored outputs:

Use System instructions to guide the model.
Provide few example inputs and outputs to guide the model. This is often referred to as few-shot prompting.
Consult our prompt engineering guide for more tips.

Structured output
In some cases, you may need structured output, such as JSON. Refer to our structured output guide to learn how.

)"""
    print(summarize(sample, "brief"))