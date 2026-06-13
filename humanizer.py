from transformers import pipeline
from prompts import PROMPTS

generator = pipeline(
    "text-generation",
    model="meta-llama/Meta-Llama-3-8B-Instruct"
)

def humanize(text, mode):

    prompt = PROMPTS[mode].format(
        text=text
    )

    result = generator(
        prompt,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    return result[0]["generated_text"]
