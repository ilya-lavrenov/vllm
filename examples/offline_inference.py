from vllm import LLM, SamplingParams

# Sample prompts.
prompts = [
    "What is OpenVINO?",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0, seed=42, max_tokens=30)

# Create an LLM.
llm = LLM(model="allenai/OLMo-1B-hf")
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

###########################
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

set_seed(42)

model_id = "allenai/OLMo-1B-hf"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

for prompt in prompts:
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(inputs, max_new_tokens=30, do_sample=False)
    text = tokenizer.batch_decode(output)
    print(text)
