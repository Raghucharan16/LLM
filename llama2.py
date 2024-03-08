import boto3 #to connect to AWS
import json  #to work with json files

prompt_data=input()  # your actual Prompt goes here

bedrock=boto3.client(service_name="bedrock-runtime") # initialising bedrock environment

# Payload is nothing but a parameter/syntax of prompt which is to be given to selected FM[Foundational Model] in this case LLama2.
# yes, payload varies for model to model.
payload={
    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)  # copying the payload information to actual body.
model_id="meta.llama2-70b-chat-v1" # copying the model-id from aws-bedrock for sprcifying the model

# invoking the model, passing the messages and extracting the response
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

#extracting the actual response for given prompt from list of tokens and printing it.
response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)
