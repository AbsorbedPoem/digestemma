# from ollama import chat, ChatResponse, Tool, Message

from meta import model
from lib.db import execute_select_to_json
import json
from client import client
from google.genai.types import GenerateContentConfig, ThinkingConfig


# tools: list[dict] = [
#     {
#         "type": "function",
#         "function": {
#         "name": "selectQuerySQL",
#         "description": "Query the SQL database and get json results",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "query": {
#                     "type": "string",
#                     "description": "the POSTGRESQL query to execute, e.g. 'SELECT * FROM users WHERE rating >= 4;'"
#                 },
#             },
#             "required": ["query"]
#         }
#         }
#     }
# ]



async def Inference(prompt):

    response = await client.aio.models.generate_content(
            model = 'gemma-4-e4b',
            contents = [prompt],
            config = GenerateContentConfig(
                system_instruction='I say high, you say low',
                max_output_tokens=3,
                thinking_config=ThinkingConfig(
                    
                )
            ),
        )

    # if response.message.tool_calls:
    #     tool_response:Message = json.loads(execute_select_to_json(response.message.tool_calls[0].function.arguments['query']))

    #     # print(response.message.tool_calls[0].function.arguments['query'])
    #     print([{"role": "user", "content": prompt}, tool_response])
    #     # return tool_response

    #     responseWithTool: ChatResponse = chat(
    #         model=model,
    #         messages=[
    #             {"role": "user", "content": prompt},
    #             tool_response if isinstance(tool_response, Message) and tool_response.role == "tool" else {"role": "tool", "content": "api_error"},
    #             {"role": "user", "content": "Puedes responder mi pregunta?"}
    #         ],
    #         stream=False
    #     )
    #     return responseWithTool

    return response
