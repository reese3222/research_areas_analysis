import json

import numpy as np


def get_topic_from_gpt(papers, community_id):
    import openai
    import os
    os.environ["OPENAI_API_KEY"] = 'sk-...'

    from openai import OpenAI
    client = OpenAI()




    prompt_topic = """Here is a list of the top 50 hubs and top 50 authorities by score for a research community in a paper citation network:

    <hubs_and_authorities>
    {HUBS_AND_AUTHORITIES}
    </hubs_and_authorities>

    Please carefully analyze the titles of the hubs and authorities to determine the main research topic that this community appears to be focused on. 

    Then, write a 100-200 word description of this research area. The description should provide an overview of the main problems, methods, and goals of the research area for a general scientific audience. Do not copy text verbatim from the hubs and authorities titles, but rather synthesize the information to provide a coherent summary in your own words.
    
    Then, write a one sentence summary of the key research topic. Maximum 10 words.


    Return a json object with the following structure:
    {{
    "description": ""
    "topic": "",
    }}

    """
    prompt = prompt_topic.format(HUBS_AND_AUTHORITIES=papers)

    resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a research assistant helping a professor with their research on machine learning."},
        {"role": "user", "content": prompt},
    ],
    response_format={ "type": "json_object" }
    )
    
    resp = resp.choices[0].message.content
    resp = resp.removeprefix("```json\n").removesuffix("```")
    resp = json.loads(resp)
    resp['community_id'] = community_id
    return resp






if __name__ == "__main__":
    papers = "papers"
    get_topic_from_gpt(papers)



