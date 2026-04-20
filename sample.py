import lmstudio as lms

model = lms.llm("qwen/qwen3-4b-2507")
result = model.respond("What is the meaning of life?")

print(result)
