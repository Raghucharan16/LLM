import boto3 #to connect to AWS
import json  #to work with json files

prompt_data=input()  # your actual Prompt goes here

bedrock=boto3.client(service_name="bedrock-runtime") # initialising bedrock environment

# Payload is nothing but a parameter/syntax of prompt which is to be given to selected FM[Foundational Model] in this case LLama2.
# payload varies for model to model.
payload={
    "prompt":prompt_data,
    "maxTokens":512,
    "temperature":0.8,
    "topP":0.8
}
body = json.dumps(payload) # copying the payload information to actual body.
model_id = "ai21.j2-mid-v1"

# invoking the model, passing the messages and extracting the response
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

#extracting the actual needed response for given prompt from list of tokens and printing it.
response_body = json.loads(response.get("body").read())
response_text = response_body.get("completions")[0].get("data").get("text")
print(response_text)
