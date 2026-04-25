# from ollama import chat, ChatResponse, Tool, Message

from lib.vars import client


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
            model = 'gemma-4-26b-a4b-it',
            contents = [prompt]
        )

    return response.text

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

